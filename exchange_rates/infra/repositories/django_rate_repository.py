"""DjangoRate Repository
"""
from exchange_rates.core.entities import Rate as RateEntity
from exchange_rates.core.repositories.rate_repository import RateRepository
from exchange_rates.core.services.currency_service import CurrencyService
from exchange_rates.models import Currency as CurrencyModel
from exchange_rates.models import Rate as RateModel


class DjangoRateRepository(RateRepository):
    """
    A repository class for handling exchange rate data using Django models.

    This repository interacts with the database to retrieve and create exchange
    rate data.

    Args:
        base_rate (CurrencyModel): The base currency for which rates are
        managed.
    """

    def __init__(self, base_rate: CurrencyModel) -> None:
        """
        Initialize the DjangoRateRepository.

        Args:
            base_rate (CurrencyModel): The base currency for which rates are
            managed.
        """
        self.base_rate = base_rate
        self.currency_service = CurrencyService()
        super().__init__()

    def get_rates(
        self, date: str = None, until_date: str = None
    ) -> RateEntity:  # no-qa
        """
        Retrieve exchange rate data from the database.

        Args:
            date (str, optional): The specific date for which rates
            are retrieved.
            until_date (str, optional): The end date for a date range
            of rates.

        Returns:
            RateEntity: Exchange rate data retrieved from the database.
        """
        if not date and not until_date:
            rate_orm = RateModel.objects.all()
        elif not until_date:
            rate_orm = RateModel.objects.filter(
                date__range=[date, date],
                base=self.base_rate.id,
            )
        else:
            rate_orm = RateModel.objects.filter(
                date__range=(date, until_date),
                base=self.base_rate.id,
            )

        if not rate_orm:
            print("INFO: Rate not loaded.")

        print("INFO: Rate successfully loaded.")
        return rate_orm

    def create_rate(
        self, base_rate: CurrencyModel, currency: CurrencyModel, date: str, price: float
    ):  # no-qa
        """
        Create a new exchange rate entry in the database.

        Args:
            base_rate (CurrencyModel): The base currency for the rate.
            currency (CurrencyModel): The target currency for the rate.
            date (str): The date for which the rate is applicable.
            price (float): The exchange rate value.

        Returns:
            RateModel: The created rate entry.
        """
        if rate_orm := (
            RateModel.objects.create(
                base=base_rate, currency=currency, date=date, price=price
            )
        ):
            print("INFO: Rate successfully created.")
            return rate_orm
        return None
