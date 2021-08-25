from django.db import models
from student.models import Student, Subject
# Create your models here.


class Exam(models.Model):
    topic = models.CharField(max_length=200)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    total_marks = models.IntegerField()
    student = models.ManyToManyField(Student)

    def __str__(self):
        return f'{self.subject}--{self.topic}'
