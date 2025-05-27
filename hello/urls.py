from django.urls import path
from . import views

urlpatterns = [
    path("userdata", views.userData, name="userData"),
    path("<str:name>", views.helloUser, name="helloUser"),
]
