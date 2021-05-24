# Generated by Django 3.1.6 on 2021-04-08 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('setting', '0021_fetchurlmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='SearchWordModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_id', models.CharField(max_length=32, verbose_name='アカウントID')),
                ('search_word', models.TextField(max_length=64, verbose_name='検索キーワード')),
                ('is_completed', models.BooleanField(default=False, verbose_name='完了フラグ')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='作成日時')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新日時')),
            ],
            options={
                'db_table': 't_search_word',
            },
        ),
    ]
