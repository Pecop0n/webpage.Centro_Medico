# Generated by Django 4.0.5 on 2022-12-12 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Intranet_Galenos', '0009_horasmedicas_fec_consulta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='horasmedicas',
            name='fec_consulta',
            field=models.DateField(blank=True, null=True),
            preserve_default=False,
        ),
    ]
