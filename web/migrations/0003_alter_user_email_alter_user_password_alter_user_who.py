# Generated by Django 4.1.2 on 2022-10-24 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_user_email_user_password_user_who'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=30),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='user',
            name='who',
            field=models.CharField(max_length=20),
        ),
    ]
