# Generated by Django 4.2.9 on 2024-02-01 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0028_rename_schaden_bewertung_auto'),
    ]

    operations = [
        migrations.AddField(
            model_name='bewertung',
            name='title',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
