# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shelters', '0002_shelter_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shelter',
            name='notes',
            field=models.CharField(max_length=1000, null=True, blank=True),
        ),
    ]
