from django.shortcuts import render
from django.http import HttpResponseRedirect  # 跳轉頁面
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import Post, Comment
from .forms import PostForm, CommentForm


def index(request):
    """The home page for blog"""
    return render(request, 'blogs/index.html')


@login_required
def posts(request):
    """Show all posts title"""
    posts = Post.objects.order_by('date_added')
    context = {'posts': posts}
    return render(request, 'blogs/posts.html', context)


@login_required
def post(request, post_id):
    """Show a single post and its content and all its comment."""
    post = Post.objects.get(id=post_id)
    comments = post.comment_set.order_by("-date_added")
    # 這裡的comment_set是model裡面所取的名稱
    context = {'post': post, 'comments': comments}
    return render(request, 'blogs/post.html', context)


@login_required
def new_post(request):
    """Add a new post."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = PostForm()
    else:
        # POST data submitted; process data.
        form = PostForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('blogs:posts'))

    context = {'form': form}
    return render(request, 'blogs/new_post.html', context)


@login_required
def new_comment(request, post_id):
    """Add a new comment for a particular post."""
    post = Post.objects.get(id=post_id)

    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = CommentForm()
    else:
        # POST data submitted; process data.
        form = CommentForm(data=request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            return HttpResponseRedirect(reverse('blogs:post', args=[post_id]))

    context = {'post': post, 'form': form}
    return render(request, 'blogs/new_comment.html', context)


@login_required
def edit_comment(request, comment_id):
    """Edit a existing comment."""
    comment = Comment.objects.get(id=comment_id)
    post = comment.post
    if request.method != 'POST':
        # Initial request; pre-fill form with the current comment.
        # instance引數能讓Django建立表單，並使用現有的紀錄項目物件中的資訊填滿表單
        form = CommentForm(instance=comment)
    else:
        # POST data submitted; process data.
        form = CommentForm(instance=comment, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('blogs:post', args=[post.id]))

    context = {'comment': comment, 'post': post, 'form': form}
    return render(request, 'blogs/edit_comment.html', context)
