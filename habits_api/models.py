from django.db import models

# Create your models here.
class Habit(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField()
    category = models.IntegerField()
    completions= models.JSONField(default=list)
    start = models.DateField()
    duration = models.IntegerField()
    days = models.JSONField(default=list)


