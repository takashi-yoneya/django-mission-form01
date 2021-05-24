# Generated by Django 3.1.6 on 2021-04-20 21:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('setting', '0028_auto_20210419_1033'),
    ]

    operations = [
        migrations.CreateModel(
            name='SyuppinCommonSettingModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_id', models.CharField(max_length=100, verbose_name='アカウントID')),
                ('sec_no', models.IntegerField(default=0, verbose_name='シーケンスNo')),
                ('column_id', models.CharField(max_length=64, verbose_name='項目ID')),
                ('column_name', models.CharField(max_length=64, verbose_name='項目名')),
                ('column_value', models.CharField(default=None, max_length=128, null=True, verbose_name='設定値')),
                ('created_at', models.DateTimeField(default=datetime.datetime.now, verbose_name='登録日')),
                ('updated_at', models.DateTimeField(default=datetime.datetime.now, verbose_name='更新日')),
            ],
            options={
                'db_table': 't_syuppin_common_setting',
            },
        ),
    ]
