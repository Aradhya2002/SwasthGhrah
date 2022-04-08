from django.db import models

class Foo(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
# Create your models here.
class register(models.Model):
    firstname= models.CharField(max_length=100)
    lastname= models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices= Foo)
    email= models.EmailField()
    contact= models.CharField(max_length=50)
    message= models.CharField(max_length=200)