from django import forms
from .models import JournalEntry


class NewJournalEntryForm(forms.ModelForm):
    class Meta:
        model = JournalEntry
        fields = [
            'feeling'
        ]
