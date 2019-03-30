"""Defines URL patterns for blogs."""

from django.urls import path, include

from . import views

app_name = "blogs" # 必須加上

urlpatterns = [
    # Home page
    path('', views.index, name='index'),

    # Show all posts
    path('posts/', views.posts, name='posts'),

    # Detail page for a single post
    path('posts/<int:post_id>/', views.post, name='post')
]