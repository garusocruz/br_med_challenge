"""Abstract Currency Repository
"""

from abc import ABC, abstractmethod

from exchange_rates.core.entities import Currency as CurrencyEntity


class CurrencyRepository(ABC):
    """Abstract base class for currency repository."""

    @abstractmethod
    def get_currency_by_name(self, name: str) -> CurrencyEntity:
        """Retrieve a currency entity using its full name.

        Args:
            name (str): The full name of the currency.

        Returns:
            CurrencyEntity: The corresponding currency entity.
        """
        raise NotImplementedError

    @abstractmethod
    def get_currency_by_short_name(self, short_name: str) -> CurrencyEntity:
        """Retrieve a currency entity using its short name.

        Args:
            short_name (str): The short short_name or code of the currency.

        Returns:
            CurrencyEntity: The corresponding currency entity.
        """
        raise NotImplementedError
