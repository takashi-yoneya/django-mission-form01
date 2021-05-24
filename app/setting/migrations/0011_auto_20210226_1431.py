# Generated by Django 3.1.6 on 2021-02-26 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('setting', '0010_asingroupmodel_yahoo_account_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='pricesettingmodel',
            name='sokketsu_price_offset',
            field=models.IntegerField(default=0, verbose_name='開始価格と即決価格の差額'),
        ),
        migrations.AlterField(
            model_name='asingroupmodel',
            name='yahoo_account_id',
            field=models.CharField(max_length=100, verbose_name='ヤフーアカウントID'),
        ),
    ]
