# Generated by Django 4.0.4 on 2022-05-10 11:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_profile_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='slug',
        ),
    ]
