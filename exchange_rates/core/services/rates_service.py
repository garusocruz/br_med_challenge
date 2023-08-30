"""Rate Service
"""
from datetime import datetime, timedelta

from exchange_rates.core.entities.rate import Rate
from exchange_rates.core.interfaces.vatcomply.client import VATClient
from exchange_rates.core.services.currency_service import CurrencyService
from exchange_rates.infra.repositories.django_rate_repository import (
    DjangoRateRepository,
)
from exchange_rates.models import Currency as CurrencyModel


class RatesService:
    """
    A service class to manage exchange rates and currency data.

    Attributes:
        base_rate (str): The short name of the base currency.
    """

    def __init__(self, base_rate: str) -> None:
        """
        Initialize the RatesService with a base currency.

        Args:
            base_rate (str): The short name of the base currency.
        """
        self._currency_service = CurrencyService()
        self.base_rate = self._currency_service.get_currency_by_short_name(
            short_name=base_rate
        )
        self._rate_repository = DjangoRateRepository(base_rate=self.base_rate)
        self._vat_client = VATClient

    def proccess(self, date: datetime, until_date: datetime) -> [Rate]:
        """
        Get or create exchange rates for specified date range and
        search days.

        Args:
            date (datetime): The starting date of the rate
            retrieval.
            until_date (datetime): The ending date of the rate
            retrieval.

        Returns:
            [Rate]: A list of Rate objects.

        Raises:
            Exception: If the date interval is more than 5 days or
            if invalid week days are provided.
        """
        search_days_list: list = []
        if date:
            search_days_list = self.get_days(date, until_date)

            # 1º bussiness rule
            # you just can filter by date intervals of up to 5 days.
            self.search_days_list_is_valid(search_days_list)

            self.get_or_create_rate(date, search_days_list)

            query = self._rate_repository.get_rates(
                date=date, until_date=until_date
            )  # no-qa
        else:
            query = self._rate_repository.get_rates()

        return query

    def get_or_create_rate(self, date, search_days_list):
        """
        Retrieves or creates exchange rates for a given date and list
        of search days.

        This method checks if exchange rates for the specified date already
        exist in the database.
        If not, it fetches exchange rates from an external VAT client and
        creates new rate records
        in the database.

        Args:
            date (datetime.date): The date for which exchange rates are to
            be retrieved or created.
            search_days_list (list): List of dates to search for existing
            rates in the database.

        Returns:
            None
        """
        for item in search_days_list:
            query = self._rate_repository.get_rates(date=item)

            if not query:
                client = self._vat_client(
                    base_rate=self.base_rate.short_name, date=date
                )
                response_rate = client.rate()

                for key, value in response_rate.get("rates").items():
                    try:
                        self.currency = (
                            self._currency_service.get_currency_by_short_name(
                                short_name=key
                            )
                        )
                        if self.currency:
                            self._rate_repository.create_rate(
                                base_rate=self.base_rate,
                                currency=self.currency,
                                date=item,
                                price=value,
                            )

                    except CurrencyModel.DoesNotExist:
                        continue

    @staticmethod
    def search_days_list_is_valid(search_days_list):
        """
        Validates a list of search days for a filtering interval.

        This method checks if the provided list of search days is
        valid for creating
        a filtering interval. The interval can be at most 5 days
        long and should
        only include weekdays (Monday to Friday).

        Args:
            search_days_list (list): A list of days to be validated.

        Raises:
            Exception: If the search days list violates the interval
            length or weekday criteria.
            The error message indicates the constraint violation.

        Example:
            # Valid input
                search_days_list_is_valid(
                    ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
                )
            # Raises exception
                search_days_list_is_valid(['Sat', 'Sun'])

        """
        if len(search_days_list) > 5:
            raise Exception(
                "You can only filter intervals of up to 5 days, \
                    including only on week days (Mon, Tue, Wed, Thu, Fri)"
            )

    def get_days(self, date, until_date):
        """
        Generates a list of days between the given 'date' and 'until_date'
        (inclusive).

        Args:
            date (datetime.date): The starting date.
            until_date (datetime.date, optional): The ending date
            (inclusive).
            If not provided, the list will contain only the 'date'.

        Returns:
            list: A list of datetime.date objects representing the days
            in the range.
        """
        if until_date:
            search_days_list = self.extract_week_days(date, until_date)
        else:
            search_days_list.append(date)
        return search_days_list

    @staticmethod
    def extract_week_days(date, until_date):
        """
        Extract a list of valid week days between the specified date range.

        Args:
            date (datetime): The starting date of the range.
            until_date (datetime): The ending date of the range.

        Returns:
            list: A list of valid weekdays.

        Raises:
            Exception: If until_date is less than date.
        """
        if until_date < date:
            raise Exception("You can only use a until date bigger than date")

        filter_interval = (until_date - date).days

        # 2º bussiness rule
        # the application just can fetch data on week days
        # week days: (Mon:0, Tue:1, Wed:2, Thu:3, Fri:4)
        allowed_week_days = [0, 1, 2, 3, 4]
        search_days_list = []

        filter_interval_iterator = 0
        while filter_interval_iterator <= filter_interval:
            if filter_interval_iterator == 0:
                _date = date
            else:
                _date = _date + timedelta(days=1)

            if _date.weekday() in allowed_week_days:
                search_days_list.append(_date)
            filter_interval_iterator += 1
        return search_days_list
