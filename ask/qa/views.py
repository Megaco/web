from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def test(request, *args, **kwargs):
    return HttpResponse('OK')

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")