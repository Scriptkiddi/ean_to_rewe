# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_auto_20151210_1607'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product2Ean2Nan',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('ean', models.CharField(max_length=32)),
                ('nan', models.CharField(max_length=32)),
                ('product', models.ForeignKey(to='product.Product')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='product2ean2nan',
            unique_together=set([('product', 'nan')]),
        ),
    ]
