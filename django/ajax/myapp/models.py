from django.db import models

# Create your models here.
class product(models.Model):
    name = models.CharField(max_length=20)

class contry(models.Model):
    name = models.CharField(max_length=20)

class state(models.Model):
    contry = models.ForeignKey(contry,on_delete=models.CASCADE)
    name = models.CharField(max_length=20)

class city(models.Model):
    state = models.ForeignKey(state,on_delete=models.CASCADE)
    name = models.CharField(max_length=20)