import logging


logger = logging.getLogger("drf_requests")


class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        logger.debug(f"{request.user}:{
                     request.body} --- {request.method}:{request.path}")

        response = self.get_response(request)
        logger.debug(f"{response.content}")
        return response
