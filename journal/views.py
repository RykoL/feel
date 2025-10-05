from django.shortcuts import render, redirect, get_object_or_404

import logging

from .forms import NewJournalEntryForm
from .models import Journal


logger = logging.getLogger(__name__)


# Create your views here.
def journal(request):
    Journal.objects.get_or_create(author=request.user)
    context = {"entries": [], "username": request.user.first_name}
    return render(request, "journal/index.html", context)


def new_journal_entry(request, journal_id):
    journal = get_object_or_404(Journal, id=journal_id, author=request.user)

    context = {"journal_id": journal.id}

    if request.method == "POST":
        form = NewJournalEntryForm(request.POST)

        if form.is_valid():
            entry = form.save()

            return redirect("journal_entry_feelings", pk=entry.id)
        else:
            # Since the feeling currently is a set of fixed buttons and the journal_id
            # is infered from the user there is not a lot of feedback we can report back
            # to the user except for: "Something wen't wrong".
            logger.error(f"Failed to save JournalEntry: {form.errors}")
            return render(request, "journal/entry/new_entry.html", context=context, status=500)


    return render(request, "journal/entry/new_entry.html", context)


def feelings(request, pk: int):
    return render(request, "journal/feelings/good.html")
