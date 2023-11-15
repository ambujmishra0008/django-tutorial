
from django.urls import path

from . import views


urlpatterns = [
    path('get_author', views.get_author),
]
