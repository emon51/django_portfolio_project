

from django.urls import path
from . import views

urlpatterns = [
    path('skill/', views.skill, name = 'skill'),
    path('project/', views.project, name = 'project')
]