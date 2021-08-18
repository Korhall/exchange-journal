from django.urls import path, include
from django.conf.urls import include, url
from .views import index, MyData, MyDataHandler, main

urlpatterns = [
    path('', index),

]