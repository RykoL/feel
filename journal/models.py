from django.db import models
from django.contrib.auth import get_user_model


class Journal(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return f"Journal for {self.author.username}"


class JournalEntry(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    journal = models.ForeignKey(Journal, on_delete=models.CASCADE)


class Feelings(models.TextChoices):
    GOOD = "good"
    NORMAL = "normal"
    OK = "ok"
    BAD = "bad"


class Trigger(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Observation(models.Model):
    feeling = models.TextField(choices=Feelings)
    journal_entry = models.OneToOneField(
        JournalEntry, on_delete=models.CASCADE, primary_key=True
    )

    triggers = models.ManyToManyField(Trigger, related_name="observations")
