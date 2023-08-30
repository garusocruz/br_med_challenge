"""Currency Service
"""
from exchange_rates.infra.repositories.django_currency_repository import (
    DjangoCurrencyRepository,
)


class CurrencyService(DjangoCurrencyRepository):
    """
    A service class that provides methods for retrieving currency information.
    Inherits from DjangoCurrencyRepository for database interactions.
    """

    def get_currency(self, name: str = None, short_name: str = None):
        """
        Retrieves currency information based on provided parameters.

        Args:
            name (str, optional): The full name of the currency.
            Defaults to None.
            short_name (str, optional): The short name or code of
            the currency. Defaults to None.

        Returns:
            dict: Currency information in the form of a dictionary.

        Raises:
            Exception: If neither name nor short_name is provided.
        """
        if not name and not short_name:
            raise Exception("A field(name, short_name) must to be provided.")

        if name:
            query = self.get_currency_by_name(name=name)
        elif short_name:
            query = self.get_currency_by_short_name(short_name=short_name)
        return query
