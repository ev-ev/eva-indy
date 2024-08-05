"""App URLs"""

# Django
from django.urls import path

# AA Evaindy App
from evaindy import views

app_name: str = "evaindy"

urlpatterns = [
    path("", views.index, name="index"),
]
