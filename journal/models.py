from django.db import models
from django.contrib.auth import get_user_model


class Journal(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)


class JournalEntry(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    journal = models.ForeignKey(Journal, on_delete=models.CASCADE)


class Observation(models.Model):
    class Feelings(models.TextChoices):
        GOOD = "good"
        NORMAL = "normal"
        OK = "ok"
        BAD = "bad"

    feeling = models.TextField(choices=Feelings)
    journal_entry = models.ForeignKey(JournalEntry, on_delete=models.CASCADE)


class Trigger(models.Model):
    name = models.CharField(max_length=50)
    observation = models.ManyToManyField(Observation)
