from django.db import models
from exam.models import Exam
from student.models import Student
# Create your models here.


class ExamResult(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.SET_NULL, null=True)
    student = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True)
    marks_obtained = models.IntegerField()

    # def __str__(self):
    #     return f'{self.student}--{self.exam}'
