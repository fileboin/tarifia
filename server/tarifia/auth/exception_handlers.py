from fastapi import Request, Response
from fastapi.responses import RedirectResponse

from tarifia.kit.http import add_query_parameters

from .exceptions import TarifiaAuthRedirectionError


async def auth_redirection_error_exception_handler(
    request: Request, exc: Exception
) -> Response:
    assert isinstance(exc, TarifiaAuthRedirectionError)
    error_url = add_query_parameters(exc.url, error=exc.message, **exc.extra)
    return RedirectResponse(error_url, exc.status_code)


__all__ = ["TarifiaAuthRedirectionError", "auth_redirection_error_exception_handler"]
