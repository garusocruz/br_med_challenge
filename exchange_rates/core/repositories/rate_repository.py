"""Abstract Rate Repository
"""
from abc import ABC, abstractmethod

from exchange_rates.core.entities import Rate


class RateRepository(ABC):
    """Abstract base class for rate repository."""

    @abstractmethod
    def get_rates(
        self,
        date: str,
    ) -> Rate:
        """
        Retrieve exchange rate data for a given date.

        Args:
            date (str): The date for which exchange rates are to be retrieved.

        Returns:
            Rate: An instance of the Rate entity containing exchange rate data.

        Raises:
            NotImplementedError: This method must be implemented by subclasses.
        """
        return NotImplementedError

    @abstractmethod
    def create_rate(self, base_rate: str, currency: str, date: str, price: float):
        """
        Create a new exchange rate entry for a specific date and price.

        Args:
            date (str): The date for which the exchange rate is being created.
            price (float): The exchange rate value.
            base_rate (str): The currency base to use on exchange rates
            currency (str): The currency used on conversions exchange rates

        Returns:
            None

        Raises:
            NotImplementedError: This method must be implemented by subclasses.
        """
        return NotImplementedError
