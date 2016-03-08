from datetime import timedelta
from django.utils.datetime_safe import datetime
from qa.models import Session, User
import uuid
from qa.utils import salt_and_hash


def do_login(username, password):
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return None
    hashed_pass = salt_and_hash(password)
    if user.password != hashed_pass:
        return None
    session = Session()
    session.key = uuid.uuid1()
    session.user = user
    session.expires = datetime.now() + timedelta(days=5)
    session.save()
    return session.key


def do_signup(username, password, email):
    hashed_pass = salt_and_hash(password)
    user = User()
    user.username = username
    user.password= hashed_pass
    user.email=email
    user.save()
    return do_login(username,password)

def findusername(request):
    sessid = request.COOKIE.get('sessid')
    try:
        session= Session.objects.get(sessid=sessid)
    except :
        return None
    id=session.id
    user=User.objects.get(id=id)
    return user.username