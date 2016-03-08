__author__ = 'ozzy'
from django.conf.urls import url


from . import views

urlpatterns = [
    url(r'^signup/', views.signup, name='signup'),
    url(r'^login/', views.login, name='signup'),
    url(r'^question/(?P<slug>\w+)/', views.question, name='question'),
    url(r'^ask/', views.ask, name='ask'),
    url(r'^popular/', views.popular, name='popular'),
    url(r'^new/', views.index, name='new'),
    url(r'^answer/', views.answer, name='new'),
    url(r'^$', views.list_new,name='list_new')
]
