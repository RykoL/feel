from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="journal_index"),
    path("feelings/good", views.feeling_good),
]
