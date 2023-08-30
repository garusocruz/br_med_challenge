"""
Module: exchange_rates.core.models

This module defines Django models representing currency-related data such
as Currency and Rate.
"""
from django.db import models

from exchange_rates.core.entities import Currency as CurrencyEntity
from exchange_rates.core.entities import Rate as RateEntyty
from exchange_rates.core.repositories.models.base import BaseModel


class Currency(BaseModel):
    """
    Represents a currency entity in the database.

    Attributes:
        name (str): The full name of the currency.
        short_name (str): The short name or code of the currency.
        symbol (str): The currency symbol.
    """

    name = models.CharField(max_length=20, unique=True)
    short_name = models.CharField(max_length=3, unique=True)
    symbol = models.CharField(max_length=3, unique=True)

    def __str__(self) -> str:
        """
        Returns a string representation of the currency.
        """
        return f"{self.name} | {self.short_name} | {self.symbol}"

    def to_entity(self):
        """
        Converts the Currency model to a corresponding CurrencyEntity.

        Returns:
            CurrencyEntity: An instance of CurrencyEntity representing
            this currency.
        """
        return CurrencyEntity(
            name=self.name,
            short_name=self.short_name,
            symbol=self.symbol,
            created=self.created.isoformat(),
            updated=self.updated.isoformat(),
            id=self.id,
        )


class Rate(BaseModel):
    """
    Represents an exchange rate between two currencies for a specific date.

    Attributes:
        base (Currency): The base currency for the exchange rate.
        date (date): The date of the exchange rate.
        currency (Currency): The target currency of the exchange rate.
        price (Decimal): The exchange rate price.
    """

    base = models.ForeignKey(
        Currency, on_delete=models.CASCADE, related_name="base_rate"
    )
    date = models.DateField()
    currency = models.ForeignKey(
        Currency, on_delete=models.CASCADE, related_name="currency"
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self) -> str:
        """
        Returns a string representation of the exchange rate.
        """
        return f"Base: \
            {self.base.name} ({self.base.short_name}) to \
                {self.currency.name} ({self.currency.short_name}) \
                    from {self.date}"

    def to_entity(self):
        """
        Converts the Rate model to a corresponding RateEntity.

        Returns:
            RateEntity: An instance of RateEntity representing this
            exchange rate.
        """
        return RateEntyty(
            base=self.base,
            date=self.date.isoformat(),
            currency=CurrencyEntity(
                name=self.currency.name,
                short_name=self.currency.short_name,
                symbol=self.currency.symbol,
                created=self.currency.created.isoformat(),
                updated=self.currency.updated.isoformat(),
                id=self.currency.id,
            ),
            price=self.price,
            created=self.created.isoformat(),
            updated=self.updated.isoformat(),
            id=self.id,
        )
