# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shelters', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shelter',
            name='address',
            field=models.ForeignKey(default=None, to='shelters.Address'),
            preserve_default=False,
        ),
    ]
