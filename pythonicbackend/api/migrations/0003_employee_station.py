# Generated by Django 3.0.4 on 2020-04-06 23:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='station',
            field=models.CharField(max_length=30)
        ),
    ]
