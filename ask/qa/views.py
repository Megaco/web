from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_GET

# Create your views here.
from django.http import HttpResponse, Http404
from . import models
from qa.models import paginate, Answer, Question


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
    questions_list = Question.objects.all().order_by('rating').reverse()
    # paginator.baseurl = '/?page='
    questions=paginate(request,questions_list)
    return render(request, 'list_new.html', {
        # 'page': page,
        # 'paginator': paginator,
        'questions': questions,
    })

def question(request, slug):
    questionid = get_object_or_404(Question, id=slug)
    answers = models.Answer.objects.all().filter(question=questionid)

    return render(request, 'question.html', {
        # 'page': page,
        # 'paginator': paginator,
        'answers': answers,
    })