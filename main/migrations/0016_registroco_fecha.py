# Generated by Django 4.2.4 on 2023-11-22 21:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_remove_registroco_fecha'),
    ]

    operations = [
        migrations.AddField(
            model_name='registroco',
            name='Fecha',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]