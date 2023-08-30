"""
View for handling exchange rates info.
"""
from requests import codes
from rest_framework.response import Response
from rest_framework.views import APIView

from exchange_rates.core.entities.rate import Rate
from exchange_rates.core.services.rates_service import RatesService
from exchange_rates.infra.serializers.rates_request_serializer import (
    RateRequestSerializer,
)
from exchange_rates.infra.serializers.rates_response_serializer import (
    RateResponseSerializer,
)


class RatesView(APIView):
    """
    API view for retrieving exchange rates based on query parameters.

    This view handles GET requests and returns exchange rate information
    based on the provided query parameters. It supports pagination and allows
    querying rates between specific dates.

    Attributes:
        None

    Methods:
        get(request): Handles GET requests for exchange rate information.
    """

    def get(self, request) -> Rate:
        """
        Handle GET requests for exchange rate information.

        Args:
            request: The HTTP request object.

        Returns:
            Response: The HTTP response containing exchange rate information
                      or an error message.

        Raises:
            None
        """
        self.page_number = self.request.query_params.get("page_number ", 1)
        self.page_size = self.request.query_params.get("page_size ", 10)

        query_params = request.query_params.dict()
        serializer = RateRequestSerializer(data=query_params)
        serializer.is_valid(raise_exception=True)

        service = RatesService(
            base_rate=serializer.validated_data.get("rate_base", "USD")
        )
        try:
            result = service.proccess(
                date=serializer.validated_data.get("date"),
                until_date=serializer.validated_data.get("until_date", None),
            )
            status_code = codes.OK
            serializer = RateResponseSerializer(result, many=True)
            result = {"rates": serializer.data}
        # pylint: disable=W0703
        except Exception as err:
            # pylint: enable=W0703
            result = {"error": {"message": err.args}}
            status_code = codes.BAD_REQUEST

        return Response(result, status=status_code)
