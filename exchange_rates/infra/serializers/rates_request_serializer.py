"""
Serializers for handling rates request data.
"""
from rest_framework import serializers


class RateRequestSerializer(serializers.Serializer):
    """
    Serializer for handling rate request parameters.

    This serializer defines the expected input parameters for a rate request.

    Attributes:
        date (DateField, optional): The specific date for which rates are
        requested.
        rate_base (CharField, optional): The base currency for rate
        conversion.
        until_date (DateField, optional): The end date of the requested
        rate range.
    """

    date = serializers.DateField(required=False)
    rate_base = serializers.CharField(required=False)
    until_date = serializers.DateField(required=False)
