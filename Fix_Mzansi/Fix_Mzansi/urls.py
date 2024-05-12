"""
URL configuration for Fix_Mzansi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),

    # -- Home Page
    path('', include('home.urls')),

    # -- Log Issue
    path('log_issue/', include('log_issue.urls')),

    # -- Logged Issues
    path('logged_issues/', include('logged_issues.urls')),

    # -- User Authintication
    path('user/', include('user_auth.urls')),
]

urlpatterns +=\
    static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # noqa: W292
urlpatterns +=\
    static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
