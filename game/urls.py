from django.urls import path
from . import views

urlpatterns = [
    path("", views.renderindex),
    path("process", views.process),
    path("delete", views.deleted),
]
