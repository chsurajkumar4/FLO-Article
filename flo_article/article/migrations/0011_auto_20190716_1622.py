# Generated by Django 2.1.7 on 2019-07-16 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0010_blogpost_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='thumbnail',
            field=models.ImageField(upload_to='article/images'),
        ),
    ]
