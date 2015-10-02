# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('section', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='section',
            name='icon',
            field=models.ImageField(upload_to=b'section_ico', blank=True),
        ),
        migrations.AlterField(
            model_name='section',
            name='image',
            field=models.ImageField(upload_to=b'section_img', blank=True),
        ),
    ]
