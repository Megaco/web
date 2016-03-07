__author__ = 'ozzy'
from django.conf.urls import url


from . import views

urlpatterns = [
    url(r'^signup/', views.index, name='signup'),
    url(r'^login/', views.index, name='signup'),
    url(r'^question/(?P<slug>\w+)/', views.question, name='question'),
    url(r'^ask/', views.index, name='ask'),
    url(r'^popular/', views.popular, name='popular'),
    url(r'^new/', views.index, name='new'),
    url(r'^$', views.list_new,name='list_new')
]
