from django.urls import path
from .import views                                #where views is a file

urlpatterns = [
    path('', views.index, name ='index'),
]