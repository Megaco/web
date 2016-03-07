from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.urlresolvers import reverse
from django.db import models
from django.contrib.auth.models import User
from django.http import Http404


class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL,related_name='question_user_author')
    likes = models.ManyToManyField(User,related_name='question_user_likes')
    def __unicode__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('question', args=[str(self.id)])
    class Meta:
        ordering = ['-added_at']

class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    question = models.ForeignKey(Question)
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    def __unicode__(self):
        return self.text
    def get_absolute_url(self):
        return '/question/%d/' % self.pk
    class Meta:
        ordering = ['-added_at']

# class QuestionManager(models.Manager):
#     def main(self, since, limit=10):
#         qs = self.order_by('-id')
#         res = []
#         if since is not None:
#             qs = qs.filter('id__lt'= since)
#         for p in qs[:1000]:
#             if len(res):
#                 res.append(p)
#             # elif res[-1].category != p.category:
#             #     res.append(p)
#             if len(res) >= limit:
#                 break
#         return res


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
    return page