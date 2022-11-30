"""ResumeSuperSite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import include, path
from resume import views
urlpatterns = [
    path('', views.redirect_to_user_page, name='resume_redirect_url'),
    path('<str:user_login>/new/', views.resume_create, name='create_resume_url'),
    path('<str:user_login>/', views.resume_list, name='resume_list_url'),
    path('<str:user_login>/<str:resume_name>/download', views.resume_download, name='download_resume_url'),
    path('<str:user_login>/<str:resume_name>/', views.resume_view, name='see_resume_url'),
]
