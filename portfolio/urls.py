"""
URL configuration for the portfolio app.
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('download-resume/', views.download_resume, name='download_resume'),
    path('hire/', views.hire, name='hire'),
]
