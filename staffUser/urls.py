from django.urls import path
from .views import staff_homepage, user_request_edit_admin, change_status

urlpatterns = [
    path('', staff_homepage, name='staff_homepage'),
    path('<id>/edit/', user_request_edit_admin, name='user_request_edit_admin'),
    path('<id>/change/status/', change_status, name='change_status'),
]
