# Generated by Django 4.2.9 on 2024-01-30 16:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0011_auto_kilometerstand'),
    ]

    operations = [
        migrations.CreateModel(
            name='AutoImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(blank=True, null=True, upload_to='1/')),
                ('image_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='images', to='user.auto')),
            ],
        ),
    ]
