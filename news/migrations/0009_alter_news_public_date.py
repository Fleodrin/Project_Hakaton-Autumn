# Generated by Django 4.1.2 on 2022-11-24 19:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0008_alter_news_public_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='public_date',
            field=models.DateField(default=datetime.datetime(2022, 11, 24, 19, 12, 22, 425664, tzinfo=datetime.timezone.utc)),
        ),
    ]