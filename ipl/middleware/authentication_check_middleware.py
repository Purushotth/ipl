class TransactionMiddleware(object):
    """
    Middleware that sets up the Transaction object.
    """

    def process_request(self, request):
        return None

    def process_view(self, request, view_func, view_args, view_kwargs):
        return None

    def process_response(self, request, response):
        return response