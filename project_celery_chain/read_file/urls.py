from django.conf.urls import url
from . import views


app_name = 'read_files'
urlpatterns = [
    url(r'^upload/$', views.index, name='index'),
]