from django.shortcuts import render, redirect, get_object_or_404

import logging

from .forms import NewJournalEntryForm
from .models import Journal, Trigger


logger = logging.getLogger(__name__)


def journal(request):
    journal, _ = Journal.objects.get_or_create(author=request.user)
    context = {
        "entries": [],
        "username": request.user.first_name,
        "journal_id": journal.id,
    }
    return render(request, "journal/index.html", context)


def new_journal_entry(request, journal_id: int):
    journal = get_object_or_404(Journal, id=journal_id, author=request.user)

    context = {"journal_id": journal.id}

    if request.method == "POST":
        form = NewJournalEntryForm(request.POST)

        if form.is_valid():
            entry = form.save()

            return redirect(
                "journal_entry_triggers", pk=entry.id, journal_id=journal.id
            )
        else:
            # Since the feeling currently is a set of fixed buttons and the journal_id
            # is infered from the user there is not a lot of feedback we can report back
            # to the user except for: "Something wen't wrong".
            logger.error(f"Failed to save JournalEntry: {form.errors}")
            return render(
                request, "journal/entry/new_entry.html", context=context, status=500
            )

    return render(request, "journal/entry/new_entry.html", context)


def select_triggers(request, pk: int, journal_id: int):
    triggers = Trigger.objects.all()
    context = {"triggers": triggers}
    return render(request, "journal/entry/select_triggers.html", context)
