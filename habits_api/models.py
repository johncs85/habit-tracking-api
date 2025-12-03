from django.db import models

# Create your models here.
class Habit(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField()
    category = models.IntegerField()
    completed = models.BooleanField()
    start_date = models.DateField()
    end_date = models.DateField()
    duration = models.IntegerField()
