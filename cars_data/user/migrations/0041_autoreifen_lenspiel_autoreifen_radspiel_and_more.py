# Generated by Django 4.2.9 on 2024-02-02 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0040_autoreifen_belage_autoreifen_verschlies'),
    ]

    operations = [
        migrations.AddField(
            model_name='autoreifen',
            name='lenspiel',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='autoreifen',
            name='radspiel',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='autoreifen',
            name='stange',
            field=models.CharField(max_length=100, null=True),
        ),
    ]