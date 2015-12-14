# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20150910_1421'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='product',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='product',
            name='ean',
        ),
        migrations.RemoveField(
            model_name='product',
            name='nan',
        ),
    ]
