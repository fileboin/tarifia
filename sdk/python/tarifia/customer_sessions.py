from __future__ import annotations

import typing

from tarifia.base import AsyncServiceBase, SyncServiceBase, parse_response_json
from tarifia.errors import (
    HTTPValidationError,
)
from tarifia.inputs import (
    CustomerSessionCustomerExternalIDCreate,
    CustomerSessionCustomerIDCreate,
)
from tarifia.outputs import (
    CustomerSession,
)


class CustomerSessionsSync(SyncServiceBase):
    @typing.overload
    def create(
        self,
        **kwargs: typing.Unpack[CustomerSessionCustomerIDCreate],
    ) -> CustomerSession: ...

    @typing.overload
    def create(
        self,
        **kwargs: typing.Unpack[CustomerSessionCustomerExternalIDCreate],
    ) -> CustomerSession: ...

    def create(
        self,
        **kwargs: typing.Any,
    ) -> CustomerSession:
        """
        Create a customer session.

        For organizations with `member_model_enabled`, this will automatically
        create a member session for the owner member of the customer.

        **Scopes**: `customer_sessions:write`

        Args:
            **kwargs: Request body parameters

        Raises:
            HTTPValidationError: Validation Error
            TarifiaNetworkError: Raised when a network error occurs while making the request.
            TarifiaServerError: Raised when the server returns a 5xx error response.
        """
        request = self.client.build_request(
            method="POST",
            url="/v1/customer-sessions/",
            path_params={},
            query_params={},
            body=kwargs,
        )
        response = self.client.send_request(request)
        method_errors = {
            422: HTTPValidationError,
        }
        return parse_response_json(response, CustomerSession, method_errors)


class CustomerSessionsAsync(AsyncServiceBase):
    @typing.overload
    async def create(
        self,
        **kwargs: typing.Unpack[CustomerSessionCustomerIDCreate],
    ) -> CustomerSession: ...

    @typing.overload
    async def create(
        self,
        **kwargs: typing.Unpack[CustomerSessionCustomerExternalIDCreate],
    ) -> CustomerSession: ...

    async def create(
        self,
        **kwargs: typing.Any,
    ) -> CustomerSession:
        """
        Create a customer session.

        For organizations with `member_model_enabled`, this will automatically
        create a member session for the owner member of the customer.

        **Scopes**: `customer_sessions:write`

        Args:
            **kwargs: Request body parameters

        Raises:
            HTTPValidationError: Validation Error
            TarifiaNetworkError: Raised when a network error occurs while making the request.
            TarifiaServerError: Raised when the server returns a 5xx error response.
        """
        request = self.client.build_request(
            method="POST",
            url="/v1/customer-sessions/",
            path_params={},
            query_params={},
            body=kwargs,
        )
        response = await self.client.send_request(request)
        method_errors = {
            422: HTTPValidationError,
        }
        return parse_response_json(response, CustomerSession, method_errors)
