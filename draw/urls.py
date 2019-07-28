# chat/urls.py
from django.conf.urls import url

from . import views

from django.urls import path

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # url(r'^(?P<room_name>[^/]+)/$', views.room, name='room'),
    path('index2/', views.index2, name='index2'),
     path('index3/', views.index3, name='index3'),
  
]

