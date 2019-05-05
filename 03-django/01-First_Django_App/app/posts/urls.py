from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    # refers to /posts/
    path('', views.index, name='index'),
]