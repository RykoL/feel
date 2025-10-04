from django import forms
from .models import Feelings


class NewJournalEntryForm(forms.Form):
    journal_id = forms.IntegerField()
    feeling = forms.CharField(label="feeling")

    def clean_feeling(self):
        feeling = self.cleaned_data["feeling"]
        if feeling not in Feelings:
            raise forms.ValidationError(f"{feeling} is not a valid choice")

        return feeling
