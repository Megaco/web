from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Question(models.Model):
    title = models.CharField(max_length=254)
    text = models.TextField()
    added_at = models.DateTimeField(blank=True)
    rating = models.IntegerField(blank=True)
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL,related_name='question_user_author')
    likes = models.ManyToManyField(User,related_name='question_user_likes')
    def __unicode__(self):
        return self.title
    def get_absolute_url(self):
        return '/question/%d/' % self.pk
    class Meta:
        ordering = ['-added_at']

class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(blank=True)
    question = models.ForeignKey(Question)
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    def __unicode__(self):
        return self.text
    def get_absolute_url(self):
        return '/question/%d/' % self.pk
    class Meta:
        ordering = ['-added_at']
