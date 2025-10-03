from django import forms
from .models import JournalEntry


class NewJournalEntryForm(forms.Form):

    feeling = forms.CharField(label="feeling")

    def clean_feeling(self):
        feeling = self.cleaned_data['feeling']

        if feeling != 'good':
            raise forms.ValidationError(f"{feeling} is not a valid choice")

        return feeling
