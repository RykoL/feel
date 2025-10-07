from django.urls import path

from . import views

urlpatterns = [
    path("", views.journal, name="journal"),
    path("<int:journal_id>/entry/<int:entry_id>/view", views.view_journal_entry, name="view_journal_entry"),
    path("<int:journal_id>/entry/new", views.new_journal_entry, name="new_entry"),
    path(
        "<int:journal_id>/entry/<int:entry_id>/triggers",
        views.select_triggers,
        name="journal_entry_triggers",
    ),
]
