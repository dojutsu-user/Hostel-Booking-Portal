from django.urls import path, include
from django.contrib.auth import views as auth_views
from userAuthentication.views import edit

urlpatterns = [
    path('login/', auth_views.login, name='login'),
    path('logout/', auth_views.logout, name='logout'),
    path('', include('social_django.urls')),
    path('edit/', edit, name='edit'),
]