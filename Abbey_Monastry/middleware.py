# middleware.py modification

from django.utils import timezone
from Src_App.models import Visitor


class VisitorMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        ip_address = request.META.get('REMOTE_ADDR')
        session_key = request.session.session_key
        if not session_key:
            # Ensure we have a session key
            request.session.save()
            session_key = request.session.session_key

        current_page = request.path

        Visitor.objects.update_or_create(
            ip_address=ip_address,
            session_key=session_key,
            defaults={'current_page': current_page, 'last_active': timezone.now()}
        )

        response = self.get_response(request)
        return response
