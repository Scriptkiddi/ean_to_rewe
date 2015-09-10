from django.db import models
from taggit.managers import TaggableManager
# Create your models here.
import watson



class Product(models.Model):
    ean = models.CharField(max_length=32)
    nan = models.CharField(max_length=32)
    name = models.CharField(max_length=256)
    price = models.FloatField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    tags = TaggableManager()

    class Meta:
        unique_together = (('ean', 'nan'),)

watson.register(Product)