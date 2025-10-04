from django.urls import path

from . import views

urlpatterns = [
    path("", views.journal, name="journal"),
    path("<int:journal_id>/entry/new", views.new_journal_entry, name="new_entry"),
    path("entry/<int:pk>/feelings", views.feelings, name="journal_entry_feelings"),
]
