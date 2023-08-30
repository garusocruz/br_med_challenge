"""Test for rate view layer"""
from django.core.management import call_command
from django.test import Client, TestCase


class RatesViewTest(TestCase):
    """
    Test case for the RatesView class.

    This test case contains methods to test the behavior of the RatesView
    class, specifically regarding the exchange rate endpoint.

    Methods:
        setUp: A method that prepares the test environment before each
        test method.
        test_rates_view: A method that tests the exchange rate
        endpoint's response.

    """

    # pytest: disable=C0103
    def setUp(self):  # no-qa
        """
        Set up the test environment.

        This method is called before each test method to prepare the required
        resources and environment for testing.

        """
        # Load fixtures
        call_command("loaddata", "fixtures/currencies.json", verbosity=0)
        self.client = Client()

    # pytest: enable=C0103

    def test_rates_view(self):
        """
        Test the exchange rate endpoint.

        This method sends a GET request to the exchange rate endpoint with
        specific parameters and asserts the expected response.

        """
        response = self.client.get("/rates/?rate_base=USD&date=2023-08-18")

        self.assertEqual(response.status_code, 200)
        self.assertTrue("rates" in response.data)
