from django.db import models

class category(models.Model):
    name = models.CharField(max_length=50)

# Create your models here.
class product(models.Model):
    category = models.ForeignKey(category,on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=50)
    price = models.FloatField()
    qty = models.IntegerField()
    image = models.ImageField(upload_to="image",default="test.png")