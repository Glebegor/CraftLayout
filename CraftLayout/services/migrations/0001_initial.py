# Generated by Django 4.0.4 on 2022-05-05 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OrderModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=255)),
                ('BgImg', models.FileField(default='No_image.png', upload_to='orderimg')),
                ('Text', models.TextField(max_length=2000)),
            ],
        ),
    ]
