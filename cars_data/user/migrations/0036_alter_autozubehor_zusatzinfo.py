# Generated by Django 4.2.9 on 2024-02-02 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0035_alter_autozubehor_bordwerkzeug_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autozubehor',
            name='zusatzInfo',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
