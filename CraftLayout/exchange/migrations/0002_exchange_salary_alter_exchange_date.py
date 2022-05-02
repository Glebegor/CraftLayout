# Generated by Django 4.0.4 on 2022-05-01 11:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('exchange', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='exchange',
            name='salary',
            field=models.CharField(default='Agreements', max_length=255),
        ),
        migrations.AlterField(
            model_name='exchange',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
