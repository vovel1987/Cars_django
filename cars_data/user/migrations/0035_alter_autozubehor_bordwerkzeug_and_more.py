# Generated by Django 4.2.9 on 2024-02-02 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0034_alter_autozubehor_bordwerkzeug_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autozubehor',
            name='bordwerkzeug',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='autozubehor',
            name='elektronikkarte',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='autozubehor',
            name='fbaks',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='autozubehor',
            name='garantieheft',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='autozubehor',
            name='ladegerät',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='autozubehor',
            name='paletot',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='autozubehor',
            name='rad_8_fach',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='autozubehor',
            name='radiokarte',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='autozubehor',
            name='reifenfüllkit',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='autozubehor',
            name='servicemappe',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='autozubehor',
            name='verbandskasten',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='autozubehor',
            name='warndreieck',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='autozubehor',
            name='windschott',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='autozubehor',
            name='zusatzInfo',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='autozubehor',
            name='zweitschlüssel',
            field=models.BooleanField(),
        ),
    ]