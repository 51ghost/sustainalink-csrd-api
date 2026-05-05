"""Custom middleware for the SustainaLink CSRD API."""

import time
import logging
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request

logger = logging.getLogger("sustainalink.csrd")


class RequestTimingMiddleware(BaseHTTPMiddleware):
    """Logs request method, path, and duration."""

    async def dispatch(self, request: Request, call_next):
        start = time.perf_counter()
        response = await call_next(request)
        duration_ms = (time.perf_counter() - start) * 1000
        logger.info(
            "%s %s → %s [%.0fms]",
            request.method,
            request.url.path,
            response.status_code,
            duration_ms,
        )
        return response
