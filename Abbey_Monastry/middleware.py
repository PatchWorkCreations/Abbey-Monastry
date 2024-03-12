from Src_App.models import Visitor
from django.utils import timezone
from datetime import timedelta

class VisitorMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        ip_address = request.META['REMOTE_ADDR']
        last_hour = timezone.now() - timedelta(hours=1)

        # Check if this IP address has visited in the last hour
        if not Visitor.objects.filter(ip_address=ip_address, timestamp__gte=last_hour).exists():
            # If not, count it as a unique visitor
            Visitor.objects.create(ip_address=ip_address)

        response = self.get_response(request)
        return response
