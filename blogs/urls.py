"""Defines URL patterns for blogs."""

from django.urls import path, include

from . import views

app_name = "blogs"  # 必須加上

urlpatterns = [
    # Home page
    path('', views.index, name='index'),

    # Show all posts
    path('posts/', views.posts, name='posts'),

    # Detail page for a single post
    path('posts/<int:post_id>/', views.post, name='post'),

    # Page for adding a new post
    path('new_post/', views.new_post, name='new_post'),

    # Page for adding a new comment
    path('new_comment/<int:post_id>/', views.new_comment, name='new_comment'),

    # Page for editing a comment
    path('edit_comment/<int:comment_id>/',
         views.edit_comment, name='edit_comment')
]
