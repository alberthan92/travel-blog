from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^list/$', views.post_list, name='post_list'),
]