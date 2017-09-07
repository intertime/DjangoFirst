from django.conf.urls import url

from article import views

urlpatterns = [
    url(r'^1/', views.basic_one),
    url(r'^2/', views.template),
    url(r'^3/', views.simple),
    url(r'^article/get/(?P<article_id>\d+)/$', views.article),
    url(r'^article/addlike/(?P<article_id>\d+)/$', views.addlike),
    url(r'^article/addcomment/(?P<article_id>\d+)/$', views.addcomment),
    url(r'^', views.articles),

]
