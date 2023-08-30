"""Test for evaluate the currency service"""
import unittest
from datetime import datetime, timedelta

import pytest
from django.core.management import call_command

from exchange_rates.core.services.rates_service import RatesService
from exchange_rates.models import Rate


@pytest.mark.django_db
class TestRatesService(unittest.TestCase):
    """
    Unit tests for the RatesService class.
    """

    def setUp(self):
        """
        Set up the test environment by loading fixture data.
        """
        # Load fixtures
        call_command("loaddata", "fixtures/currencies.json", verbosity=0)

    def test_get_or_create_rate(self):
        """
        Test the get_or_create_rate method of RatesService.

        It checks if the method retrieves or creates a Rate instance
        for a given date range and verifies the response type.
        """
        date = datetime.strptime("2023-08-19", "%Y-%m-%d").date()
        until_date = datetime.strptime("2023-08-22", "%Y-%m-%d").date()
        service = RatesService(base_rate="USD")
        response = service.proccess(date, until_date)

        self.assertIsNotNone(response)
        self.assertIsInstance(response.first(), Rate)

    def test_until_date_bigger_than_date(self):
        """
        Test behavior when until_date is not greater than date.

        It checks if an exception is raised when trying to extract week days
        with an until_date that is not greater than the provided date.
        """
        service = RatesService(base_rate="USD")
        date = datetime.now()
        until_date = date - timedelta(days=2)

        with self.assertRaises(Exception) as context:
            service.extract_week_days(date, until_date)
        message = "You can only use a until date bigger than date"
        self.assertEqual(str(context.exception), message)
