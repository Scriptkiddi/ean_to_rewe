# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_auto_20151212_2144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eans',
            name='product',
            field=models.ForeignKey(related_name='eans', to='product.Product'),
        ),
    ]
