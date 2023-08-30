"""DjangoCurrency Repository
"""
from exchange_rates.core.entities import Currency as CurrencyEntity
from exchange_rates.core.repositories.currency_repository import (  # no-qa
    CurrencyRepository,
)
from exchange_rates.models import Currency as CurrencyModel


class DjangoCurrencyRepository(CurrencyRepository):
    """
    Repository implementation for accessing currency data in the Django ORM.

    This class extends CurrencyRepository and provides methods to retrieve
    currency
    data from the Django ORM using both the currency's full name and short
    name.

    Attributes:
        None

    Methods:
        get_currency_by_name(name: str) -> CurrencyEntity:
            Retrieves a currency by its full name from the Django ORM.

        get_currency_by_short_name(short_name: str) -> CurrencyEntity:
            Retrieves a currency by its short name from the Django ORM.
    """

    def get_currency_by_name(self, name: str) -> CurrencyEntity:
        """Retrieve a currency by its full name from the Django ORM.

        Args:
            name (str): The full name of the currency.

        Returns:
            CurrencyEntity: An instance of CurrencyEntity representing the
            retrieved currency.

        Raises:
            DoesNotExist: If no currency with the given name is found.
        """
        if currency_orm := (CurrencyModel.objects.get(name=name)):
            print("INFO: Currency successfully loaded.")
            return currency_orm
        return None

    def get_currency_by_short_name(self, short_name: str) -> CurrencyEntity:
        """Retrieve a currency by its short name from the Django ORM.

        Args:
            short_name (str): The short name of the currency.

        Returns:
            CurrencyEntity: An instance of CurrencyEntity representing the
            retrieved currency.

        Raises:
            DoesNotExist: If no currency with the given short name is found.
        """
        if currency_orm := (CurrencyModel.objects.get(short_name=short_name)):
            print("INFO: Currency successfully loaded.")
            return currency_orm
        return None
