# Generated by Django 4.2.8 on 2024-03-07 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Src_App', '0028_visitor'),
    ]

    operations = [
        migrations.AddField(
            model_name='visitor',
            name='user_agent',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]