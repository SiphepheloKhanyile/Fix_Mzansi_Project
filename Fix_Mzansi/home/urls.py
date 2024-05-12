from django.urls import path
from . import views


urlpatterns = [
    # -- Home Page View
    path('', views.home, name='home'),
]
