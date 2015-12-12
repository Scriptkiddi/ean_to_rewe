from django.db import models
from taggit.managers import TaggableManager
# Create your models here.
import watson



class Product(models.Model):
    name = models.CharField(max_length=256)
    created = models.DateTimeField(auto_now_add=True)
    nan = models.CharField(max_length=32)
    #image
    #text
    tags = TaggableManager()


class Price(models.Model):
    price = models.FloatField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey("Product", related_name="prices")


class Ean(models.Model):
    ean = models.CharField(max_length=32)
    product = models.ForeignKey("Product", related_name="eans")

watson.register(Product)