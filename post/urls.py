from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views
from .views import *

app_name = 'post'





urlpatterns = [

    url("", index, name="index"),


]