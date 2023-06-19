from django.db import models

# Create your models here.
class RegForm(models.Model):
    name = models.TextField()
    dob = models.DateField()
    age = models.IntegerField()
    gender = models.TextField()
    phone = models.IntegerField()
    email = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    district = models.TextField()
    branch = models.TextField()
    account_type = models.TextField()
    mater_provi = models.TextField()