# Generated by Django 4.2.10 on 2024-02-11 11:54

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('background', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='background',
            name='profile_image',
            field=cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='background',
            name='title',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]