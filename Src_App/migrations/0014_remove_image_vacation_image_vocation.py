# Generated by Django 4.2.8 on 2024-01-11 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Src_App', '0013_image_francis_artwork'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='vacation',
        ),
        migrations.AddField(
            model_name='image',
            name='vocation',
            field=models.ImageField(blank=True, null=True, upload_to='dynamic_images', verbose_name='Vocation Image'),
        ),
    ]
