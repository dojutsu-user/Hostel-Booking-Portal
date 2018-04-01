from django.contrib import admin
from django.urls import path, include
from .views import homepage
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', auth_views.login, name='login'),
    path('logout/', auth_views.logout, name='logout'),
    path('', include('social_django.urls')),
]