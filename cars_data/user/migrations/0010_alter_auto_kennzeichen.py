# Generated by Django 4.2.9 on 2024-01-30 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_auto_hersteller'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auto',
            name='kennzeichen',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
