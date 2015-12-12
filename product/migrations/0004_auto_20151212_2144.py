# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20150910_1421'),
    ]

    operations = [
        migrations.CreateModel(
            name='Eans',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('ean', models.CharField(max_length=32)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='product',
            unique_together=set([]),
        ),
        migrations.AddField(
            model_name='eans',
            name='product',
            field=models.ForeignKey(to='product.Product'),
        ),
        migrations.RemoveField(
            model_name='product',
            name='ean',
        ),
    ]
