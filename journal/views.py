from django.shortcuts import render, redirect


from .forms import NewJournalEntryForm
from .models import Journal, JournalEntry


# Create your views here.
def journal(request):
    Journal.objects.get_or_create(author=request.user)
    context = {"entries": [], "username": request.user.first_name}
    return render(request, "journal/index.html", context)


def new_entry(request):
    journal, _ = Journal.objects.get_or_create(author=request.user)

    context = {"journal_id": journal.pk}

    if request.method == "POST":
        form = NewJournalEntryForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            entry = JournalEntry(journal_id=data["journal_id"])
            entry.save()
            return redirect("journal_entry_feelings", pk=entry.id)

    return render(request, "journal/entry/new_entry.html", context)


def feelings(request, pk: int):
    return render(request, "journal/feelings/good.html")
