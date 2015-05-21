# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tea',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name=b'name')),
                ('kind', models.CharField(max_length=255, verbose_name=b'kind', choices=[(b'english', b'UnitedKingdom_style'), (b'chinese', b'China_style'), (b'japanese', b'Japan_style')])),
                ('price', models.IntegerField(verbose_name=b'price')),
                ('is_recommended', models.BooleanField(default=False, verbose_name=b'recommended_menu')),
            ],
        ),
    ]
