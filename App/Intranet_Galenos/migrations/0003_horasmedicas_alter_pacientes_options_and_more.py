# Generated by Django 4.0.5 on 2022-12-11 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Intranet_Galenos', '0002_alter_pacientes_id_paciente'),
    ]

    operations = [
        migrations.CreateModel(
            name='HorasMedicas',
            fields=[
                ('id_horamedica', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.AlterModelOptions(
            name='pacientes',
            options={'ordering': ['pa_nombre', '-pa_apellido'], 'verbose_name': 'Paciente', 'verbose_name_plural': 'Pacientes'},
        ),
        migrations.AlterField(
            model_name='pacientes',
            name='sexo',
            field=models.CharField(choices=[('F', 'Femenino'), ('M', 'Masculino')], default='F', max_length=1),
        ),
        migrations.AlterModelTable(
            name='pacientes',
            table='Pacientes',
        ),
    ]