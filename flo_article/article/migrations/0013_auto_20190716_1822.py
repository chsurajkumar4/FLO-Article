# Generated by Django 2.1.7 on 2019-07-16 12:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0012_auto_20190716_1631'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogpost',
            options={'ordering': ['-pub_date']},
        ),
    ]
