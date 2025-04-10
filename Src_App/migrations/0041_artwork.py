# Generated by Django 4.2.8 on 2025-03-13 11:32

import cloudinary.models
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Src_App', '0040_visitoractivity_country'),
    ]

    operations = [
        migrations.CreateModel(
            name='Artwork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('psalter', 'Psalter Artwork'), ('francis', 'Francis Artwork')], default='psalter', max_length=10)),
                ('title', models.CharField(help_text='Title of the artwork', max_length=200)),
                ('image1', cloudinary.models.CloudinaryField(help_text='First artwork image', max_length=255, verbose_name='image')),
                ('image2', cloudinary.models.CloudinaryField(blank=True, help_text='Second artwork image', max_length=255, null=True, verbose_name='image')),
                ('date_uploaded', models.DateTimeField(default=django.utils.timezone.now, help_text='Timestamp of artwork upload')),
            ],
            options={
                'ordering': ['-date_uploaded'],
            },
        ),
    ]
