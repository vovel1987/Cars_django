# Generated by Django 4.2.9 on 2024-02-02 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0033_autozubehor_zusatzinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autozubehor',
            name='bordwerkzeug',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='autozubehor',
            name='elektronikkarte',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='autozubehor',
            name='fbaks',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='autozubehor',
            name='garantieheft',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='autozubehor',
            name='ladegerät',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='autozubehor',
            name='paletot',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='autozubehor',
            name='rad_8_fach',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='autozubehor',
            name='radiokarte',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='autozubehor',
            name='reifenfüllkit',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='autozubehor',
            name='servicemappe',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='autozubehor',
            name='verbandskasten',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='autozubehor',
            name='warndreieck',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='autozubehor',
            name='windschott',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='autozubehor',
            name='zweitschlüssel',
            field=models.CharField(max_length=200),
        ),
    ]
