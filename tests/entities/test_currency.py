"""Test for currency entities"""
import unittest

from exchange_rates.core.entities import Currency


class TestCurrency(unittest.TestCase):
    """
    A unit test class to validate the initialization of the Currency entity.
    """

    def setUp(self):
        """
        Set up test data for Currency entity initialization.
        """
        self.currency_data = {
            "name": "US Dollar",
            "short_name": "USD",
            "symbol": "$",
            "created": "2023-01-01",
            "updated": "2023-08-01",
            "id": 1,
        }

    def test_currency_initialization(self):
        """
        Test the initialization of a Currency entity with provided data.
        """
        currency = Currency(
            name=self.currency_data["name"],
            short_name=self.currency_data["short_name"],
            symbol=self.currency_data["symbol"],
            created=self.currency_data["created"],
            updated=self.currency_data["updated"],
            id=self.currency_data["id"],
        )

        self.assertEqual(currency.name, self.currency_data["name"])
        self.assertEqual(currency.short_name, self.currency_data["short_name"])
        self.assertEqual(currency.symbol, self.currency_data["symbol"])
        self.assertEqual(currency.created, self.currency_data["created"])
        self.assertEqual(currency.updated, self.currency_data["updated"])
        self.assertEqual(currency.id, self.currency_data["id"])
