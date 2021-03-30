from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'article'

urlpatterns = [
    path('', views.article_list,name='list'),
    url(r'^(?P<slug>[\w-]+)/$', views.article_detail,name='detail'),
]
