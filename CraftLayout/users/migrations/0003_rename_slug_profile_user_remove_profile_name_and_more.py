# Generated by Django 4.0.4 on 2022-04-28 20:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_profile_avatar_alter_profile_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='slug',
            new_name='user',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='Name',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='Surname',
        ),
    ]
