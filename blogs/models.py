from django.db import models


class Post(models.Model):
    """A post is posted by a user"""
    title = models.CharField(max_length=20)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    # owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Return a string representation of the model."""
        return self.title


class Comment(models.Model):
    """Someone comment on a post."""
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'comments'

    def __str__(self):
        """Return a string representation of the model."""
        return self.text
