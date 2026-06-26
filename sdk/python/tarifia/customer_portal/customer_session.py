from __future__ import annotations

from tarifia.base import AsyncServiceBase, SyncServiceBase, parse_response_json
from tarifia.outputs import (
    CustomerCustomerSession,
    PortalAuthenticatedUser,
)


class CustomerSessionSync(SyncServiceBase):
    def introspect(
        self,
    ) -> CustomerCustomerSession:
        """
        Introspect the current session and return its information.

        **Scopes**: `customer_portal:read` `customer_portal:write`

        Args:

        Raises:
            TarifiaNetworkError: Raised when a network error occurs while making the request.
            TarifiaServerError: Raised when the server returns a 5xx error response.
        """
        request = self.client.build_request(
            method="GET",
            url="/v1/customer-portal/customer-session/introspect",
            path_params={},
            query_params={},
        )
        response = self.client.send_request(request)
        return parse_response_json(response, CustomerCustomerSession)

    def get_authenticated_user(
        self,
    ) -> PortalAuthenticatedUser:
        """
        Get information about the currently authenticated portal user.

        **Scopes**: `customer_portal:read` `customer_portal:write`

        Args:

        Raises:
            TarifiaNetworkError: Raised when a network error occurs while making the request.
            TarifiaServerError: Raised when the server returns a 5xx error response.
        """
        request = self.client.build_request(
            method="GET",
            url="/v1/customer-portal/customer-session/user",
            path_params={},
            query_params={},
        )
        response = self.client.send_request(request)
        return parse_response_json(response, PortalAuthenticatedUser)


class CustomerSessionAsync(AsyncServiceBase):
    async def introspect(
        self,
    ) -> CustomerCustomerSession:
        """
        Introspect the current session and return its information.

        **Scopes**: `customer_portal:read` `customer_portal:write`

        Args:

        Raises:
            TarifiaNetworkError: Raised when a network error occurs while making the request.
            TarifiaServerError: Raised when the server returns a 5xx error response.
        """
        request = self.client.build_request(
            method="GET",
            url="/v1/customer-portal/customer-session/introspect",
            path_params={},
            query_params={},
        )
        response = await self.client.send_request(request)
        return parse_response_json(response, CustomerCustomerSession)

    async def get_authenticated_user(
        self,
    ) -> PortalAuthenticatedUser:
        """
        Get information about the currently authenticated portal user.

        **Scopes**: `customer_portal:read` `customer_portal:write`

        Args:

        Raises:
            TarifiaNetworkError: Raised when a network error occurs while making the request.
            TarifiaServerError: Raised when the server returns a 5xx error response.
        """
        request = self.client.build_request(
            method="GET",
            url="/v1/customer-portal/customer-session/user",
            path_params={},
            query_params={},
        )
        response = await self.client.send_request(request)
        return parse_response_json(response, PortalAuthenticatedUser)
