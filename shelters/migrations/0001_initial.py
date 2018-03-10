# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import address.models


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shelter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('allows_men', models.BooleanField()),
                ('allows_women', models.BooleanField()),
                ('allows_children', models.BooleanField()),
                ('allows_couples', models.BooleanField()),
                ('allows_pets', models.BooleanField()),
                ('notes', models.CharField(max_length=1000)),
                ('address', address.models.AddressField(to='address.Address')),
            ],
        ),
    ]
