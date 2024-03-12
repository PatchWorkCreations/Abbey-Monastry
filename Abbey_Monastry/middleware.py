from Src_App.models import Visitor


class VisitorMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Get relevant information from the request
        ip_address = request.META.get('REMOTE_ADDR', None)
        user_agent = request.META.get('HTTP_USER_AGENT', None)

        # Save visitor information to the database
        if ip_address and user_agent:
            visitor = Visitor.objects.create(ip_address=ip_address, user_agent=user_agent)
            request.session['visitor_id'] = visitor.id

        response = self.get_response(request)
        return response
