from django.db import models

# Create your models here.

class patientInfo(models.Model):
    userName = models.CharField(max_length=120)
    bodyBmi = models.IntegerField()
    bodyInfo = models.CharField(max_length=120)