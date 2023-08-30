"""Currency Entity
"""


class Currency:
    """
    Represents a currency with associated properties.

    Attributes:
        name (str): Full name of the currency.
        short_name (str): Short name or code of the currency.
        symbol (str): Symbol representing the currency.
        created (str): Timestamp of when the currency was created.
        updated (str): Timestamp of when the currency was last updated.
        _id (int): Unique identifier for the currency.
    """

    def __init__(
        self,
        created: str,
        id: int,
        name: str,
        short_name: str,
        symbol: str,
        updated: str,
    ) -> None:
        """
        Initializes a Currency object with provided attributes.

        Args:
            name (str): Full name of the currency.
            short_name (str): Short name or code of the currency.
            symbol (str): Symbol representing the currency.
            created (str): Timestamp of when the currency was created.
            updated (str): Timestamp of when the currency was last updated.
            id (int): Unique identifier for the currency.
        """
        # pylint: disable=C0103
        self.id = id  # no-qa
        # pylint: enable=C0103
        self.created = created
        self.name = name
        self.short_name = short_name
        self.symbol = symbol
        self.updated = updated
