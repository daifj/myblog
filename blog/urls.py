from django.urls import path, re_path
from django.conf.urls import url
from . import views

app_name = 'blog'
urlpatterns = [
    re_path(r'^index/$', views.index, name='index'),
    re_path(r'^article/(?P<article_id>\d+)$', views.article_page, name='article_page'),
    # path(r'article/<int:article_id>', views.article_page, name='article_page')
    re_path(r'^edit/(?P<article_id>\d+)$', views.edit_page, name='edit_page'),
    re_path(r'^edit/action$', views.edit_action, name='edit_action'),
]
