# Generated by Django 4.2.4 on 2023-10-14 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_acciones_delete_objetivos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acciones',
            name='Huella',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]
