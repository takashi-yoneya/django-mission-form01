# Generated by Django 3.1.6 on 2021-04-19 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('syuppin', '0008_auto_20210419_0420'),
    ]

    operations = [
        migrations.AddField(
            model_name='syuppinitemmodel',
            name='condition',
            field=models.CharField(default='', max_length=20, verbose_name='商品の状態'),
        ),
    ]