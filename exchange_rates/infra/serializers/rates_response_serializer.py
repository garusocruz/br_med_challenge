"""
Serializers for handling rates response data.
"""
from rest_framework import serializers

from exchange_rates.infra.serializers.currency_response_serializer import (
    RateCurrencyResponseSerializer,
)
from exchange_rates.models import Rate


class RateResponseSerializer(serializers.ModelSerializer):
    """
    Serializer for converting Rate model instances into JSON representation.

    This serializer includes fields from the Rate model and also embeds
    serialized currency information using RateCurrencyResponseSerializer.

    Attributes:
        base: Serialized representation of the base currency related to the
        rate.
        currency: Serialized representation of the target currency related
        to the rate.
    """

    base = RateCurrencyResponseSerializer()
    currency = RateCurrencyResponseSerializer()

    class Meta:
        """
        Meta:
        model (Rate): The model class associated with this serializer.
        fields (list or tuple): Specifies the fields to include in the
        serialized output.
            Here, '__all__' is used to include all fields defined in
            the model.
        """

        model = Rate
        fields = "__all__"
