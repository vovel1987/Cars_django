# Generated by Django 4.2.9 on 2024-02-15 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0057_remove_auto_schaden'),
    ]

    operations = [
        migrations.AddField(
            model_name='auto',
            name='schaden',
            field=models.BooleanField(null=True),
        ),
    ]
