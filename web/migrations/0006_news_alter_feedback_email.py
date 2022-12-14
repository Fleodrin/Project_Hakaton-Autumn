# Generated by Django 4.1.2 on 2022-10-24 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_feedback_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('main_text', models.CharField(max_length=10000)),
                ('preview', models.CharField(max_length=150)),
            ],
        ),
        migrations.AlterField(
            model_name='feedback',
            name='email',
            field=models.EmailField(max_length=100, null=True),
        ),
    ]
