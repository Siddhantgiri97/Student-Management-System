
from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from student.models import Student
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField(max_length=2000)
    date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(
        upload_to="post", blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:50] + '...'


class Comment(models.Model):
    comment = models.TextField(max_length=2000)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    thumb = models.ImageField(
        upload_to="comment", blank=True, null=True)
    timestamp = models.DateTimeField(default=now)

    def __str__(self):
        return self.comment
