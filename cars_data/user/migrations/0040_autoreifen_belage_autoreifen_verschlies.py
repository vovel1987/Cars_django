# Generated by Django 4.2.9 on 2024-02-02 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0039_autoreifen'),
    ]

    operations = [
        migrations.AddField(
            model_name='autoreifen',
            name='belage',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='autoreifen',
            name='verschlies',
            field=models.CharField(max_length=100, null=True),
        ),
    ]