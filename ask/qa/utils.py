from django.http import Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import hashlib, uuid


def paginate(request, qs):
    try:
        limit = int(request.GET.get('limit', 10))
    except ValueError:
        limit = 10
    if limit > 100:
        limit = 10
    try:
        page = int(request.GET.get('page', 1))
    except ValueError:
        raise Http404
    paginator = Paginator(qs, limit)
    try:
        page = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        page = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        page = paginator.page(paginator.num_pages)
    return paginator, page

def salt_and_hash(password):
    password= password.encode('utf-8')
    salt = "salt".encode('utf-8')
    hashed_password = hashlib.sha512(password+salt).hexdigest()
    return hashed_password

