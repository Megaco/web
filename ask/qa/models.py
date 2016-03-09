from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models
#
# class User(models.Model):
#     username = models.CharField(unique=True, max_length=254)
#     password = models.CharField(max_length=254)
#     email = models.EmailField()
# class Session(models.Model):
#     key = models.CharField(unique=True, max_length=254)
#     user = models.ForeignKey(User)
#     expires = models.DateTimeField()


class Question(models.Model):
    title = models.CharField(max_length=254)
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User,related_name='question_user_author')
    likes = models.ManyToManyField(User,related_name='question_user_likes', default=0)
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



