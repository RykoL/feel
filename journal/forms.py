from django import forms
from django.db import transaction
from .models import JournalEntry, Observation, Feelings


class NewJournalEntryForm(forms.ModelForm):
    class Meta:
        model = JournalEntry
        fields = ["journal"]

    feeling = forms.CharField(label="feeling")

    def save(self, commit=True):
        """
        Overrides the default save method to also create an Observation.
        """
        with transaction.atomic():
            instance = super().save(commit=False)

            if commit:
                instance.save()

                Observation.objects.create(
                    journal_entry=instance, feeling=self.cleaned_data["feeling"]
                )

        return instance

    def clean_feeling(self):
        feeling = self.cleaned_data["feeling"]
        if feeling not in Feelings:
            raise forms.ValidationError(f"{feeling} is not a valid choice")

        return feeling
