# Generated by Django 4.1.3 on 2022-12-20 03:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='studinfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True, default=datetime.datetime(2022, 12, 20, 9, 23, 45, 963829))),
                ('name', models.CharField(max_length=20)),
                ('sub', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=20)),
            ],
        ),
    ]