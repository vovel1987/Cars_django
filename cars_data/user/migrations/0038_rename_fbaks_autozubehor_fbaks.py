# Generated by Django 4.2.9 on 2024-02-02 13:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0037_alter_autozubehor_zusatzinfo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='autozubehor',
            old_name='fbaks',
            new_name='FBAKS',
        ),
    ]
