from django.db import models
from student.models import Subject
# Create your models here.


class FilesAdmin(models.Model):
    adminUpload = models.FileField(upload_to='downloads')
    title = models.CharField(max_length=50)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    topic = models.CharField(max_length=100, default="")

    def __str__(self):
        return self.title
