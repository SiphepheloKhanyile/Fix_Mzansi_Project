"""
Linking Urls to views for Logging issues
"""
from django.urls import path
from . import views


urlpatterns = [
    # -- Home Page View
    path('', views.log_issue_view, name='log_issue'),
    path('update_issue/<int:post_id>/',
         views.update_issue, name='update_issue'),
    path('delete_issue/<int:post_id>/',
         views.delete_issue, name='delete_issue'),
]
