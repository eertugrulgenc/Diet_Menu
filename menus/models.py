from django.db import models
from django.forms import CharField

# Create your models here.

class foodInfo(models.Model):
    foodName = models.CharField(max_length=100)
    foodCalorie = models.IntegerField()