"""Test for evaluate the currency service"""
import unittest

import pytest
from django.core.management import call_command

from exchange_rates.core.services.currency_service import CurrencyService
from exchange_rates.models import Currency


@pytest.mark.django_db
class TestCurrencyService(unittest.TestCase):
    """
    Unit tests for the CurrencyService class.

    These tests cover the functionality of the CurrencyService class,
    specifically focusing on retrieving currency information.

    Note: These tests require a Django database connection.

    Test methods:
    - test_get_currency_by_name
    - test_get_currency_by_short_name
    - test_get_currency_without_name_and_short_name
    """

    def setUp(self):
        """
        Set up test data by loading currency fixtures into the database.
        """
        # Load fixtures
        call_command("loaddata", "fixtures/currencies.json", verbosity=0)

    def test_get_currency_by_name(self):
        """
        Test retrieving a currency by its name using the CurrencyService.
        """
        service = CurrencyService()
        response = service.get_currency(name="Euro")

        self.assertIsNotNone(response)
        self.assertIsInstance(response, Currency)

    def test_get_currency_by_short_name(self):
        """
        Test retrieving a currency by its short name using the CurrencyService.
        """
        service = CurrencyService()
        response = service.get_currency(short_name="EUR")

        self.assertIsNotNone(response)
        self.assertIsInstance(response, Currency)

    def test_get_currency_without_name_and_short_name(self):
        """
        Test the exception raised when neither name nor short name is provided.
        """
        # Arrange
        currency_service = CurrencyService()

        # Act and Assert
        with self.assertRaises(Exception) as context:
            currency_service.get_currency()

            self.assertEqual(
                str(context.exception),
                "A field(name, short_name) \
                    must be provided.",
            )  # no-qa
