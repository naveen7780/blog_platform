from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
class User(AbstractUser):
    role_choices = [
        ('admin', 'Admin'),
        ('author', 'Author'),
        ('reader', 'Reader'),
    ]
    role = models.CharField(max_length=10, choices=role_choices, default='reader')

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    content = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
