from django.db import models

# Create your models here.
class Todo(models.Model):
    date = models.DateTimeField()
    description = models.CharField(max_length=250)
    priority = models.IntegerField()