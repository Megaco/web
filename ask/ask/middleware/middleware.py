from django.http import HttpRequest
from django.utils.datetime_safe import datetime
from qa.models import Session


class CheckSessionMiidleware(object):
    def process_request(self, request):
        try:
            sessid = request.COOKIES.get('sessid')
            session = Session.objects.get(key=sessid,expires__gt=datetime.now(),)
            request.session = session
            request.username = session.user
        except Session.DoesNotExist:
            request.session = None
            request.username = None