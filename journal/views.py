from django.shortcuts import render, redirect

from .forms import NewJournalEntryForm
from .models import JournalEntry

# Create your views here.
def journal(request):
    entries = JournalEntry.objects.all()
    context = {
        'entries': entries
    }
    return render(request, "journal/index.html", context)


def new_entry(request):
    if request.method == 'POST':
        form = NewJournalEntryForm(request.POST)
        if form.is_valid():
            journal_entry = form.save()
            return redirect("journal_entry_feelings", pk=journal_entry.id)

    return render(request, "journal/entry/new_entry.html")


def feelings(request, pk: int):
    return render(request, "journal/feelings/good.html")
