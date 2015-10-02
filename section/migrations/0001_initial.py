# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50, blank=True)),
                ('description', models.CharField(max_length=50, blank=True)),
                ('icon', models.ImageField(upload_to=b'section_ico')),
                ('image', models.ImageField(upload_to=b'section_img')),
            ],
        ),
    ]
