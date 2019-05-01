from django.db import models
from .storage import ImageStorage

# Create your models here.

class User(models.Model):

    user_name = models.CharField(max_length=20, unique=True)
    user_image = models.ImageField(upload_to='userfaces/', storage=ImageStorage())
    introduce = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True) # 建立時間戳記並照時間排序
    
    def __str__(self):
        return self.user_name