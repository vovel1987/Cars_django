# Generated by Django 4.2.9 on 2024-02-06 14:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0048_remove_auto_thumbnail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='auto',
            name='slug',
        ),
    ]
