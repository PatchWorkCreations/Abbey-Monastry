# Generated by Django 4.2.8 on 2024-03-13 14:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Src_App', '0032_visitor_current_page_visitor_last_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='visitor',
            name='session_key',
            field=models.CharField(default=django.utils.timezone.now, max_length=40),
            preserve_default=False,
        ),
    ]
