# Generated by Django 4.2.4 on 2023-10-31 23:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0012_configuracion_valor_alter_configuracion_preferencias_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='configuracion',
            name='Valor',
        ),
        migrations.AlterField(
            model_name='configuracion',
            name='Preferencias',
            field=models.CharField(default='t,'),
        ),
        migrations.AlterField(
            model_name='configuracion',
            name='Usuario',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
