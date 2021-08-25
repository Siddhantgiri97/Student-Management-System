from django.urls import path
from .import views

app_name = 'community'
urlpatterns = [
    path("", views.home, name="home"),
    path("<int:pk>/post/", views.view_post, name="view_post"),
    path("addPost/", views.add_post, name="add_post"),
    path("searchPost/", views.search_post, name="search_post"),

]
