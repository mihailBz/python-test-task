from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import date


# Create your models here.


class User(AbstractUser):
    pass


class Post(models.Model):
    title = models.CharField(max_length=100)
    link = models.CharField(max_length=500)
    creation_date = models.DateField(default=date.today)
    amount_of_upvotes = models.PositiveIntegerField(default=0)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)


class Comment(models.Model):
    content = models.TextField()
    creation_date = models.DateField(default=date.today)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)


class Upvote(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
