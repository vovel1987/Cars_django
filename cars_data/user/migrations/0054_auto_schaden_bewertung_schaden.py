# Generated by Django 4.2.9 on 2024-02-13 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0053_alter_bewertung_preis'),
    ]

    operations = [
        migrations.AddField(
            model_name='auto',
            name='schaden',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='bewertung',
            name='schaden',
            field=models.BooleanField(null=True),
        ),
    ]
