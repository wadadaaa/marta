# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('section', '0004_aboutsection'),
    ]

    operations = [
        migrations.CreateModel(
            name='Catalog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=80, blank=True)),
                ('slug', models.SlugField(unique=True)),
                ('image', models.ImageField(upload_to=b'category_pic', verbose_name='Image', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, blank=True)),
                ('slug', models.SlugField(unique=True)),
                ('image', models.ImageField(upload_to=b'product_pic', verbose_name='Image', blank=True)),
                ('description', models.TextField(help_text=b'Describe product', blank=True)),
                ('price', models.DecimalField(max_digits=15, decimal_places=2)),
                ('sale_price', models.DecimalField(null=True, max_digits=15, decimal_places=2)),
                ('is_active', models.BooleanField(default=True)),
                ('is_featured', models.BooleanField(default=False)),
                ('quantity', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('catalog', models.ForeignKey(to='section.Catalog')),
            ],
        ),
    ]
