# Generated by Django 4.1.2 on 2022-10-24 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0007_news_image_news_public_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='files/'),
        ),
    ]
