from django.db import models
from django.db.models import SET_NULL
from users.models import User
from categories.models import Category

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    slug = models.ImageField(upload_to='posts/images/')
    