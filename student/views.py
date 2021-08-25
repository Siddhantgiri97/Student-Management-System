from django.shortcuts import render, redirect, HttpResponseRedirect
from .models import Student, Notification
from result.models import ExamResult
from exam.models import Exam
from .forms import StudentRegistration, AddNotification
from .filters import ExamResultFilter
from exam.forms import ExamForm
from django.forms import inlineformset_factory
import json
# Create your views here.


def student(request):
    students = Student.objects.all()
    context = {'students': students}
    return render(request, "student/student.html", context)


def show_student(request, pk):
    student = Student.objects.get(id=pk)
    examresults = student.examresult_set.all()
    context = {'student': student, 'examresults': examresults}
    return render(request, "student/show_student.html", context)


def add_student(request):
    if request.method == 'POST':
        form = StudentRegistration(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('student')
    else:
        form = StudentRegistration()
    context = {'form': form}
    return render(request, 'student/addStudent.html', context)


def update_student(request, pk):
    if request.method == 'POST':
        student = Student.objects.get(id=pk)
        form = StudentRegistration(
            request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
        return redirect('student')
    else:
        student = Student.objects.get(id=pk)
        form = StudentRegistration(instance=student)
    context = {'form': form}
    return render(request, "student/updatestudent.html", context)


def delete_data(request, id):
    if request.method == 'POST':
        pi = Student.objects.get(pk=id)
        pi.delete()
    return HttpResponseRedirect('/')


def ranklist(request):
    submitted = 'submitted' in request.GET
    data = request.GET if submitted else None
    ranklist = ExamResult.objects.all().order_by("-marks_obtained")
    myFilter = ExamResultFilter(data, queryset=ranklist)
    ranklist = myFilter.qs
    context = {'myFilter': myFilter, 'ranklist': ranklist}
    return render(request, "student/ranklist.html", context)


def add_exam(request):
    exams = Exam.objects.all()
    if request.method == 'POST':
        form = ExamForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('add_exam')
    else:
        form = ExamForm()
    context = {'form': form, 'exams': exams}
    return render(request, 'student/addExam.html', context)


def add_result(request, pk):
    students = Student.objects.all()
    ExamResultFormSet = inlineformset_factory(
        Exam, ExamResult, fields=('student', 'marks_obtained'), extra=students.count())
    exam = Exam.objects.get(id=pk)
    formset = ExamResultFormSet(
        queryset=ExamResult.objects.none(), instance=exam)
    if request.method == 'POST':
        formset = ExamResultFormSet(request.POST, instance=exam)
        if formset.is_valid():
            formset.save()
            return redirect('add_exam')
    else:
        formset = ExamResultFormSet(instance=exam)

    context = {'formset': formset, 'exam': exam}
    return render(request, "student/addResult.html", context)


def performance(request, pk):
    student = Student.objects.get(id=pk)
    # examresults = student.examresult_set.all()
    phyresults = student.examresult_set.filter(
        exam__subject__subject="Physics")[:5]
    chemresults = student.examresult_set.filter(
        exam__subject__subject="Chemistry")[:5]
    mathresults = student.examresult_set.filter(
        exam__subject__subject="Mathematics")[:5]
    context = {'student': student, 'phyresults': phyresults,
               'chemresults': chemresults, 'mathresults': mathresults}
    return render(request, "student/performance.html", context)


def view_notification(request):
    if request.method == 'POST':
        form = AddNotification(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    else:
        form = AddNotification()
    notifications = Notification.objects.all()
    context = {'notifications': notifications, 'form': form}
    return render(request, 'student/notification.html', context)


def delete_notification(request, id):
    if request.method == 'POST':
        pi = Notification.objects.get(pk=id)
        pi.delete()
    return HttpResponseRedirect('/')
