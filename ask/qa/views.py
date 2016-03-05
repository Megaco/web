from django.shortcuts import render
from django.views.decorators.http import require_GET

# Create your views here.
from django.http import HttpResponse

def test(request, *args, **kwargs):
    return HttpResponse('OK')

@require_GET
def index(request):

    return HttpResponse("Hello, world. You're at the polls index.")