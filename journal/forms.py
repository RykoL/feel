from django import forms
from django.db import transaction
from .models import JournalEntry, Observation, Feelings


class NewJournalEntryForm(forms.ModelForm):
    class Meta:
        model = JournalEntry
        # This form will not render any fields to the user, as the 'journal'
        # will be handled internally and 'created_at' is automatic.
        fields = ["journal"]

    feeling = forms.CharField(label="feeling")

    def save(self, commit=True):
        """
        Overrides the default save method to also create an Observation.
        """
        # A transaction ensures that either both objects are created successfully, or none are.
        with transaction.atomic():
            instance = super().save(commit=False)

            if commit:
                instance.save()  # Save the JournalEntry to the database.

                # Step 2: Now that the entry is saved, create the related Observation.
                Observation.objects.create(
                    journal_entry=instance, feeling=self.cleaned_data["feeling"]
                )

        return instance

    def clean_feeling(self):
        feeling = self.cleaned_data["feeling"]
        if feeling not in Feelings:
            raise forms.ValidationError(f"{feeling} is not a valid choice")

        return feeling
