from django.urls import path
from . import views

urlpatterns = [
    path("", views.hng_public_api, name="hng_public_api"),
]