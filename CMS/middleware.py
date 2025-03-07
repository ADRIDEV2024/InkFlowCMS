import logging
from django.utils.timezone import now

logger = logging.getLogger(__name__)

class RequestLoggingMiddleware:
    """
    Middleware para registrar cada solicitud HTTP en los logs.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request_time = now()
        response = self.get_response(request)
        logger.info(f"{request.method} {request.path} - {response.status_code} - {request_time}")
        return response
