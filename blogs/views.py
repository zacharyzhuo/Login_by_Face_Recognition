from django.shortcuts import render

from .models import Post

def index(request):
    """The home page for blog"""
    return render(request, 'blogs/index.html')

def posts(request):
    """Show all posts title"""
    posts = Post.objects.order_by('date_added')
    context = {'posts': posts}
    return render(request, 'blogs/posts.html', context)

def post(request, post_id):
    """Show a single post and its content and all its comment."""
    post = Post.objects.get(id=post_id)
    comments = post.comment_set.order_by("-date_added")
    # 這裡的comment_set是model裡面所取的名稱
    context = {'post': post, 'comments': comments}
    return render(request, 'blogs/post.html', context)
