"""
Serializers for handling currency rate response data.
"""
from rest_framework import serializers

from exchange_rates.models import Currency


class RateCurrencyResponseSerializer(serializers.ModelSerializer):
    """
    Serializer for converting Currency model data into JSON response format.

    This serializer takes a Currency model instance and converts its fields
    into JSON format, suitable for API responses.

    Attributes:
        Meta: A inner class used to associate the serializer with the
        Currency model and specify the fields to include in the serialized
        output.
        - model: The Currency model class to serialize.
        - fields: A special keyword that indicates all fields of the model
        should be included in the serialized output.

    Example:
        Given a Currency instance 'currency_instance':
        ```
        serializer = RateCurrencyResponseSerializer(currency_instance)
        response_data = serializer.data
        ```
        The 'response_data' will contain the serialized JSON representation
        of 'currency_instance' according to the specified model fields.
    """

    class Meta:
        """
        Meta class to associate the serializer with the Currency model and
        specify the fields to include in the serialized output.
        """

        model = Currency
        fields = "__all__"
