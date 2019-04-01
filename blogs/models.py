from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    """A post is posted by a user"""
    title = models.CharField(max_length=20)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE) # 文章作者

    def __str__(self):
        """Return a string representation of the model."""
        return self.title


class Comment(models.Model):
    """Someone comment on a post."""
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE) # 留言作者

    class Meta:
        verbose_name_plural = 'comments'

    def __str__(self):
        """Return a string representation of the model."""
        return self.text
