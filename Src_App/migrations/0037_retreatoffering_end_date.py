# Generated by Django 4.2.8 on 2024-08-19 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Src_App', '0036_retreatoffering_registration_link_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='retreatoffering',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]