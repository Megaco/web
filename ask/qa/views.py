from datetime import timedelta
from django.contrib.auth import authenticate, login
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404
from django.utils.datetime_safe import datetime
from django.views.decorators.http import require_GET, require_POST

# Create your views here.
from django.http import HttpResponse, Http404, HttpResponseRedirect
from . import models
from qa.forms import AskForm, AnswerForm
from qa.models import Answer, Question, User
from .utils import paginate


def test(request, *args, **kwargs):
    return HttpResponse('OK')

@require_GET
def index(request):

    return HttpResponse("Hello, world. You're at the polls index.")

@require_GET
def list_new(request):
    questions_list = models.Question.objects.all()
    # paginator.baseurl = '/?page='
    paginator, questions=paginate(request,questions_list)
    return render(request, 'list_new.html', {
        # 'page': page,
        # 'paginator': paginator,
        'questions': questions,
    })

@require_GET
def popular(request):
    questions_list = Question.objects.all().order_by('-rating')
    # paginator.baseurl = '/?page='
    paginator, questions=paginate(request,questions_list)
    return render(request, 'list_new.html', {
        # 'page': page,
        # 'paginator': paginator,
        'questions': questions,
    })


def question(request, slug):
    question = get_object_or_404(Question, id=slug)
    # answers = models.Answer.objects.all().filter(question=question)
    answers = question.answer_set.all()
    form = AnswerForm(initial={'question': str(slug)})
    return render(request, 'question.html', {
        'question': question,
        'answers': answers,
        'form': form,
    })

def ask(request):
    if request.method == "POST":
        form = AskForm(request.POST)
        form.author=request.user
        if form.is_valid():
            # question = form.save()
            url = question.get_absolute_url()
            return HttpResponseRedirect(url)
            # return HttpResponseRedirect(reverse('question', args=[post.id]))
    else:
        form = AskForm()
    return render(request, 'ask_form.html', {
    'form': form
    })

@require_POST
def answer(request):
    form = AnswerForm(request.POST)
    form.author = request.user
    if form.is_valid():
        post = form.save()
        #url = post.get_url()
        return HttpResponseRedirect(reverse('question', args=[post.question.id]))
    return HttpResponseRedirect('/')


def login_user(request):
    error = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        url = request.POST.get('continue', '/')

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                return HttpResponseRedirect('/')
    return render(request, 'login.html', {'error': error,})

def signup(request):
    error = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        # url = request.POST.get('continue', '/')
        user = User.objects.create_user(username, email=email, password=password)
        login(request, user)
        return HttpResponseRedirect('/')
    return render(request, 'signup.html', {'error': error })
