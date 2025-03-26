import logging
import traceback
from datetime import datetime

logger = logging.getLogger(__name__)

class APILoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request_time = datetime.now()
        logger.info(f"[API REQUEST] {request.method} {request.path} at {request_time}")

        try:
            response = self.get_response(request)
        except Exception as e:
            # Log the exception details
            error_time = datetime.now()
            error_traceback = traceback.format_exc()  # Full error traceback
            logger.error(f"[API ERROR] {request.method} {request.path} at {error_time}")
            logger.error(f"Exception: {str(e)}")
            logger.error(f"Traceback:\n{error_traceback}")

            # Return a custom error response (optional)
            from django.http import JsonResponse
            return JsonResponse({'error': 'Internal Server Error'}, status=500)

        response_time = datetime.now()
        logger.info(f"[API RESPONSE] {request.method} {request.path} - {response.status_code} at {response_time}")

        return response
