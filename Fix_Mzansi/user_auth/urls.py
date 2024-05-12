"""
Linking Urls to views for Logging issues
"""
from django.urls import path
from . import views


urlpatterns = [
    # -- Auth Views
    path('signin/', views.signin_view, name='signin'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.user_settings, name='profile'),
]
