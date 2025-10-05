from django.shortcuts import render, redirect, get_object_or_404


from .forms import NewJournalEntryForm
from .models import Journal


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

    return render(request, "journal/entry/new_entry.html", context)


def feelings(request, pk: int):
    return render(request, "journal/feelings/good.html")
