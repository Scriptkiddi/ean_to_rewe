from django.db import models
from taggit.managers import TaggableManager
# Create your models here.
import watson



class Product(models.Model):
    name = models.CharField(max_length=256)
    price = models.FloatField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    tags = TaggableManager()


class Product2Ean2Nan(models.Model):
    ean = models.CharField(max_length=32)
    nan = models.CharField(max_length=32)
    product = models.ForeignKey("Product")

    class Meta:
        unique_together = (('product', 'nan'),)
watson.register(Product)