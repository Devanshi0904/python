from django.db import models

# Create your models here.
class Dept (models.Model):
    name = models.CharField(max_length=50)
    hod = models.CharField(max_length=50)

class Emp (models.Model):
    dept = models.ForeignKey(Dept,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    age = models.IntegerField()