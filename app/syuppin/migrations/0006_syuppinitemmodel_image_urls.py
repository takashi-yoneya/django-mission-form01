# Generated by Django 3.1.6 on 2021-04-19 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('syuppin', '0005_auto_20210416_0105'),
    ]

    operations = [
        migrations.AddField(
            model_name='syuppinitemmodel',
            name='image_urls',
            field=models.TextField(default='', verbose_name='画像'),
        ),
    ]
