from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_GET, require_POST

# Create your views here.
from django.http import HttpResponse, Http404, HttpResponseRedirect
from . import models
from qa.forms import AskForm, AnswerForm
from qa.models import Answer, Question
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

@require_GET
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
        if form.is_valid():
            question = form.save()
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
    if form.is_valid():
        post = form.save()
        #url = post.get_url()
        return HttpResponseRedirect(reverse('question', args=[post.question.id]))
    return HttpResponseRedirect('/')
