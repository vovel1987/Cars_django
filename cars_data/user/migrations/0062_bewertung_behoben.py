# Generated by Django 4.2.9 on 2024-02-16 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0061_alter_bewertung_zusatzreparatur'),
    ]

    operations = [
        migrations.AddField(
            model_name='bewertung',
            name='behoben',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
