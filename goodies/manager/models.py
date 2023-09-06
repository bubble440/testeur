from django.db import models

class Product(models.Model):
    name = models.fields.CharField(max_length=100)
    #image = models.fields.ImageField(upload_to="")
    price = models.fields.IntegerField()
    description = models.fields.CharField(max_length=1000)
    category = models.fields.CharField(max_length=20)