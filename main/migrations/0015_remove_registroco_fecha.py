# Generated by Django 4.2.4 on 2023-11-22 21:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_configuracion_deuda_alter_registroco_repositorio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registroco',
            name='Fecha',
        ),
    ]