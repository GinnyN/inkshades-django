# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-29 02:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(verbose_name=b'Orden')),
                ('page', models.ImageField(blank=True, upload_to=b'pages/', verbose_name='P\xe1ginas')),
                ('chapter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='front.Chapter')),
            ],
        ),
    ]
