# Generated by Django 4.2.9 on 2024-02-02 09:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0031_alter_bewertung_element_in_component'),
    ]

    operations = [
        migrations.CreateModel(
            name='AutoZubehor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('zweitschlüssel', models.BooleanField()),
                ('paletot', models.BooleanField()),
                ('rad_8_fach', models.BooleanField()),
                ('windschott', models.BooleanField()),
                ('fbaks', models.BooleanField()),
                ('reifenfüllkit', models.BooleanField()),
                ('servicemappe', models.BooleanField()),
                ('elektronikkarte', models.BooleanField()),
                ('bordwerkzeug', models.BooleanField()),
                ('warndreieck', models.BooleanField()),
                ('radiokarte', models.BooleanField()),
                ('ladegerät', models.BooleanField()),
                ('verbandskasten', models.BooleanField()),
                ('garantieheft', models.BooleanField()),
                ('auto', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='zubehors', to='user.auto')),
            ],
        ),
    ]
