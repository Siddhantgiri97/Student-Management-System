from django.urls import path
from .import views


urlpatterns = [
    path("", views.student, name="student"),
    path("ranklist/", views.ranklist, name="ranklist"),
    path("performance/<int:pk>/", views.performance, name="performance"),
    path("notification/", views.view_notification, name="view_notification"),
    path("addExam/", views.add_exam, name="add_exam"),
    path("showStudent/<int:pk>/", views.show_student, name="show_student"),
    path("addStudent/", views.add_student, name="add_student"),
    path("updateStudent/<int:pk>/", views.update_student, name="update_student"),
    path('delete/<int:id>/', views.delete_data, name="deletedata"),
    path('delete_notification/<int:id>/',
         views.delete_notification, name="delete_notification"),
    path('<int:pk>/addResult', views.add_result, name="add_result"),
]
