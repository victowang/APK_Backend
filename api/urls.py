from django.urls import path

from . import views

urlpatterns = [

    path('applications', views.applications, name='applications'),
]