# Generated by Django 4.2.9 on 2024-01-30 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_model_fahrz'),
    ]

    operations = [
        migrations.AddField(
            model_name='auto',
            name='title',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
