# Generated by Django 3.2.2 on 2021-05-18 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default=None, max_length=20),
        ),
    ]
