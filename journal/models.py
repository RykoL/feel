
from django.db import models

# Create your models here.

class JournalEntry(models.Model):

    class Feelings(models.TextChoices):
        GOOD = "good"
        NORMAL = "normal"
        OK = "ok"
        BAD = "bad"

    feeling = models.CharField(choices=Feelings)
    created_at = models.DateTimeField(auto_now_add=True)


class Triggers(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    journal_entry = models.ForeignKey(JournalEntry, on_delete=models.CASCADE)
