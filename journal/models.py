from django.db import models

# Create your models here.

class Feeling(models.Model):

    class Feelings(models.TextChoices):
        GOOD = "Good"
        NORMAL = "Normal"
        OK = "Ok"
        BAD = "Bad"

    id = models.AutoField(primary_key=True)
    name = models.CharField(choices=Feelings)


class Event(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField()
