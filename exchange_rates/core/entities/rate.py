"""Rate Entity
"""
from .currency import Currency as CurrencyEntity


class Rate:
    """
    Represents a currency exchange rate.

    Attributes:
        base (str): The base currency code for the exchange rate.
        date (str): The date associated with the exchange rate.
        currency (CurrencyEntity): The currency entity for which
        the rate is defined.
        price (str): The exchange rate price.
        created (str): The timestamp indicating when the rate was
        created.
        updated (str): The timestamp indicating when the rate was
        last updated.
        id (int): The unique identifier for the rate.
    """

    def __init__(
        self,
        base: str,
        created: str,
        currency: CurrencyEntity,
        date: str,
        id: int,
        price: str,
        updated: str,
    ):
        """
        Initialize a Rate object.

        Args:
            base (str): The base currency code for the exchange rate.
            date (str): The date associated with the exchange rate.
            currency (CurrencyEntity): The currency entity for which
            the rate is defined.
            price (str): The exchange rate price.
            created (str): The timestamp indicating when the rate was
            created.
            updated (str): The timestamp indicating when the rate was
            last updated.
            id (int): The unique identifier for the rate.
            *args: Additional positional arguments (unused).
            **kwargs: Additional keyword arguments (unused).
        """
        # pylint: disable=C0103
        self.id = id
        # pylint: enable=C0103
        self.base = base
        self.date = date
        self.created = created
        self.currency = currency
        self.price = price
        self.updated = updated
