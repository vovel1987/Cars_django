# Generated by Django 4.2.9 on 2024-02-01 14:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0027_alter_bewertung_preis'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bewertung',
            old_name='schaden',
            new_name='auto',
        ),
    ]
