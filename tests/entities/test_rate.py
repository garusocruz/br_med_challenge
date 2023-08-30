"""Test for rate entities"""
import unittest

from exchange_rates.core.entities import Currency, Rate


class TestRate(unittest.TestCase):
    """Test suite for the Rate class."""

    def test_init(self):
        """Test the initialization of the Rate class."""
        currency_mock = Currency(
            name="US Dollar",
            short_name="USD",
            symbol="$",
            created="2023-08-30",
            updated="2023-08-30",
            id=1,
        )

        expected_base = "USD"
        expected_date = "2023-08-30"
        expected_price = "1.25"
        expected_created = "2023-08-30"
        expected_updated = "2023-08-30"
        expected_id = 1

        rate = Rate(
            base=expected_base,
            date=expected_date,
            currency=currency_mock,
            price=expected_price,
            created=expected_created,
            updated=expected_updated,
            id=expected_id,
        )

        self.assertEqual(rate.base, expected_base)
        self.assertEqual(rate.date, expected_date)
        self.assertEqual(rate.currency, currency_mock)
        self.assertEqual(rate.price, expected_price)
        self.assertEqual(rate.created, expected_created)
        self.assertEqual(rate.updated, expected_updated)
        self.assertEqual(rate.id, expected_id)
