"""
Linking Urls to views for Logging issues
"""
from django.urls import path
from . import views


urlpatterns = [
    # -- Home Page View
    path('', views.logged_issues_view, name='logged_issues'),
]
