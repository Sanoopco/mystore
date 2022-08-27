from django.db import models

# Create your models here.
class Mobiles(models.Model):
    name=models.CharField(max_length=200)
    brand=models.CharField(max_length=200)
    band=models.CharField(max_length=200)
    display=models.CharField(max_length=100)
    price=models.PositiveIntegerField()
    rating=models.FloatField(null=True)
