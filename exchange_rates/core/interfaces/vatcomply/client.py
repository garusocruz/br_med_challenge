"""A client to consume a VAT service api
https://www.vatcomply.com/documentation
"""
from datetime import datetime

import requests
from decouple import config

codes = requests.codes


class VATClient:
    """
    A client for retrieving VAT (Value Added Tax) rates.

    This client allows fetching VAT rates for different currencies and dates
    from a specified base URL.

    Attributes:
        base_url (str): The base URL for the VAT service.
        base_rate (str): The base currency code for VAT rate conversions.
        date (datetime.date): The date for which VAT rates are to be fetched.

    Methods:
        rate(): Fetches VAT rates for the specified base currency and date.

    Usage:
        client = VATClient(base_rate="USD")
        vat_rates = client.rate()
    """

    base_url = config("VAT_BASE_URL")

    def __init__(self, base_rate: str = "USD", date=None) -> None:
        """
        Initializes a new instance of the VATClient.

        Args:
            base_rate (str, optional): The base currency code for VAT
            rate conversions.
            date (datetime.date, optional): The date for which VAT
            rates are to be fetched.
        """
        self.base_rate = base_rate

        if not date:
            date = datetime.now().date()

        self.date = date

    def rate(self):
        """
        Fetches VAT rates for the specified base currency and date.

        Returns:
            dict: A dictionary containing VAT rates for different currencies.
        """
        url = f"{self.base_url}/rates"

        querystring = {"base": self.base_rate, "date": self.date.isoformat()}
        response = requests.get(url, params=querystring)

        if response.status_code not in [
            codes.OK,
            codes.CREATED,
            codes.ACCEPTED,
            codes.NO_CONTENT,
        ]:
            return NotImplementedError

        return response.json()
