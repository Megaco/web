from django import forms
from django.shortcuts import get_object_or_404
from qa.models import Answer, Question

class AskForm(forms.Form):
    title = forms.CharField(max_length=255)
    text =  forms.CharField(widget=forms.Textarea)
    author = forms.CharField(widget=forms.Textarea)
    def clean_title(self):
        title = self.cleaned_data['title']
        if title.strip()=='':
            raise forms.ValidationError(u'Title is empty', code = 12)
        return title

    def clean_text(self):
        text = self.cleaned_data['text']
        if text.strip()=='':
            raise forms.ValidationError(u'Text is empty', code = 12)
        return text

    def save(self):
        # self.cleaned_data['author_id'] = 1
        post = Question(**self.cleaned_data)
        post.save()
        return post

class AnswerForm(forms.Form):
    question = forms.IntegerField(widget=forms.HiddenInput)
    text = forms.CharField(widget=forms.Textarea)
    author = forms.CharField(widget=forms.Textarea)
    def clean_question(self):
        question = self.cleaned_data['question']
        if question == 0:
            raise forms.ValidationError(u'Answer need question', code = 12)
        return question
    def clean_text(self):
        text = self.cleaned_data['text']
        if text.strip()=='':
            raise forms.ValidationError(u'Text is empty', code = 12)
        return text
    def save(self):
        self.cleaned_data['question'] = get_object_or_404(Question, pk=self.cleaned_data['question'])
        # self.cleaned_data['author_id'] = 1
        answer = Answer(**self.cleaned_data)
        answer.save()
        return answer
