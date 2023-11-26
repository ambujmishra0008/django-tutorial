
from django.urls import path

from . import views


urlpatterns = [
    # path('get_author', views.get_author),
    path('register', views.register, name = "register"),
    # path("submitaction", views.submitaction, name = "submitaction")
]
app_name = "blog"
