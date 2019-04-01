"""Defines URL patterns for users."""

from django.urls import path, include
from django.contrib.auth.views import LoginView

from . import views

app_name = "users"  # 必須加上

urlpatterns = [
    # Login page
    path('login/', LoginView.as_view(template_name='users/login.html'),
         name='login'),
    # Logout
    path('logout/', views.logout_view, name='logout'),

    # Registration page
    path('register/', views.register, name='register'),
]
