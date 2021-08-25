from django.urls import path
from django.contrib.auth import views as auth_views
from .import views
urlpatterns = [
    path("", views.home, name="home"),
    path('login/', views.loginPage, name="login"),
    path('register/', views.registerPage, name="register"),
    path('logout/', views.logoutUser, name="logout"),

    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="home/reset_password.html"),
         name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="home/password_reset_done.html"),
         name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="home/password_reset_confirm.html"),
         name="password_reset_confirm"),
    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name="home/password_reset_complete.html"), name="password_reset_complete"),
]
