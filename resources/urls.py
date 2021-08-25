from django.urls import path
from django.views.static import serve
from django.conf import settings
from django.conf.urls import url

from .import views
app_name = 'resources'
urlpatterns = [
    path("", views.home, name="home"),
    url(r'^download/(?P<path>.*)$', serve,
        {'document_root': settings.MEDIA_ROOT}),
]
