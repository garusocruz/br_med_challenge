"""Test for called requests from provider VAT"""
import unittest
from unittest.mock import MagicMock, patch

from exchange_rates.core.interfaces.vatcomply.client import VATClient


class TestVATClient(unittest.TestCase):
    """
    Unit tests for the VATClient class.
    """

    @patch("requests.get")
    def test_rate(self, mock_get):
        """
        Test the rate() method of VATClient.

        This test verifies that the rate() method of VATClient returns the
        expected result by mocking the requests.get function and simulating
        a response with pre-defined data.

        The expected_result variable contains a dictionary representing
        exchange rates.
        The mock_response is used to simulate a successful response from
        the external API.
        The client.rate() method is then called and compared against the
        expected result.

        If the result matches the expected result, the test passes.

        :param mock_get: Mocked requests.get function.
        """
        expected_result = {
            "date": "2023-08-18",
            "base": "USD",
            "rates": {
                "EUR": 0.9202171712524155,
                "USD": 1.0,
                "JPY": 145.49553694671943,
                "BGN": 1.7997607435354743,
                "CZK": 22.11926014539431,
                "DKK": 6.856906229870249,
                "GBP": 0.7867212662188277,
                "HUF": 352.9861047207141,
                "PLN": 4.1131867120640475,
                "RON": 4.550289868408944,
                "SEK": 10.985828655562713,
                "CHF": 0.8807398546056869,
                "ISK": 132.2352075089721,
                "NOK": 10.656114843102973,
                "TRY": 27.10361645348302,
                "AUD": 1.5642771694119812,
                "BRL": 4.976166375264563,
                "CAD": 1.355755958406184,
                "CNY": 7.287843931167755,
                "HKD": 7.831508235943683,
                "IDR": 15319.002484586363,
                "ILS": 3.795435722830588,
                "INR": 83.07950676359621,
                "KRW": 1340.7932272016196,
                "MXN": 17.077482285819453,
                "MYR": 4.647464801693199,
                "NZD": 1.6885985092481826,
                "PHP": 56.34121652710039,
                "SGD": 1.3574123493144383,
                "THB": 35.35014263366154,
                "ZAR": 19.06073433330266,
            },
        }

        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = expected_result
        mock_get.return_value = mock_response

        client = VATClient()
        result = client.rate()

        self.assertEqual(result, expected_result)
