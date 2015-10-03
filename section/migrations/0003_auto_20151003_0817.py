# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('section', '0002_auto_20151002_1310'),
    ]

    operations = [
        migrations.CreateModel(
            name='MainSection',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50, blank=True)),
                ('description', models.CharField(max_length=50, blank=True)),
                ('image', models.ImageField(upload_to=b'section_img', blank=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Section',
        ),
    ]
