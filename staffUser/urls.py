from django.urls import path
from .views import staff_homepage

urlpatterns = [
    path('', staff_homepage, name='staff_homepage')
]
