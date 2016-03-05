__author__ = 'ozzy'
from django.conf.urls import url


from . import views

urlpatterns = [
    url(r'^signup/', views.index, name='signup'),
    url(r'^login/', views.index, name='signup'),
    url(r'^question/([^/]+)/', views.test, name='question'),
    url(r'^ask/', views.index, name='ask'),
    url(r'^popular/', views.index, name='popular'),
    url(r'^new/', views.index, name='new'),
    url(r'^$', views.test,name='index')
]
