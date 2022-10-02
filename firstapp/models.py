from django.db import models

# Create your models here.
class contactdata(models.Model):
    fname=models.CharField(max_length=120)
    sname=models.CharField(max_length=120)
    email=models.CharField(max_length=100)
    mobile=models.CharField(max_length=120)
    username=models.CharField(max_length=130)
    password=models.CharField(max_length=130)
    
class contactform(models.Model):
    name=models.CharField(max_length=30)
    emailid=models.CharField(max_length=30)
    mobileno=models.BigIntegerField()