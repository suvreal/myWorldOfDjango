from django.db import models

# Create your models here.

class PeopleApp(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  cityname = models.CharField(max_length=255)
  streetname = models.CharField(max_length=255)
  housecode = models.IntegerField(max_length=32)
  citycode = models.IntegerField(max_length=32)
  isadult = models.BooleanField(null=False)
  levelofeducation =  models.CharField(max_length=128)
  currentproffession = models.CharField(max_length=128)
  