from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from django.views.decorators.http import require_GET

# Create your views here.
from django.http import HttpResponse, Http404
from . import models
from qa.models import paginate


def test(request, *args, **kwargs):
    return HttpResponse('OK')

@require_GET
def index(request):

    return HttpResponse("Hello, world. You're at the polls index.")

def list_new(request):
    questions_list = models.Question.objects.all()
    # paginator.baseurl = '/?page='
    questions=paginate(request,questions_list)
    return render(request, 'list_new.html', {
        # 'page': page,
        # 'paginator': paginator,
        'questions': questions,
    })

def popular(request):
    questions_list = models.Question.objects.all().order_by('rating')
    # paginator.baseurl = '/?page='
    questions=paginate(request,questions_list)
    return render(request, 'list_new.html', {
        # 'page': page,
        # 'paginator': paginator,
        'questions': questions,
    })

def question(request, slug):
    answers = models.Answer.objects.all().filter(question=slug)

    return render(request, 'question.html', {
        # 'page': page,
        # 'paginator': paginator,
        'answers': answers,
    })