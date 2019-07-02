from django.urls import path
from .import views                                #where views is a file

urlpatterns = [
    path('', views.home, name ='home'),
    path('add', views.addition, name ='add'),
]