# Generated by Django 2.1.7 on 2019-07-16 10:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0009_blogpost_thumbnail'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
