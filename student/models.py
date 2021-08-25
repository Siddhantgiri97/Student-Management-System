from django.db import models

from django.contrib.auth.models import User


# Create your models here.
CLASS_CHOICES = [
    ("11th", '11th'),
    ("12th", '12th'),
    ("Repeater", 'Repeater'),
]

SUBJECT_CHOICES = [
    ("Mathematics", 'Mathematics'),
    ("Physics", 'Physics'),
    ("Chemistry", 'Chemistry'),
]


class Student_Class(models.Model):
    stu_class = models.CharField(
        max_length=50, choices=CLASS_CHOICES, null=True)

    def __str__(self):
        return self.stu_class


class Subject(models.Model):
    subject = models.CharField(
        max_length=50, choices=SUBJECT_CHOICES, null=True)

    def __str__(self):
        return self.subject


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200)
    stu_class = models.ForeignKey(Student_Class, on_delete=models.CASCADE,null=True)
    rollNo = models.IntegerField(default=0)
    batch = models.CharField(max_length=10)
    contact = models.CharField(max_length=100)
    address = models.CharField(max_length=300)
    email = models.CharField(max_length=100)
    image = models.ImageField(
        upload_to="profile", null=True, blank=True, default="stars.png")

    def __str__(self):
        return self.name


class Notification(models.Model):
    text = models.TextField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
