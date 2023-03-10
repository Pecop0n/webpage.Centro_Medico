# Generated by Django 4.0.5 on 2022-12-11 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Intranet_Galenos', '0003_horasmedicas_alter_pacientes_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Medicos',
            fields=[
                ('id_medico', models.AutoField(primary_key=True, serialize=False)),
                ('me_nombre', models.CharField(max_length=20)),
                ('me_apellido', models.CharField(max_length=30)),
                ('me_rut', models.IntegerField()),
                ('me_edad', models.IntegerField()),
                ('sexo', models.CharField(choices=[('F', 'Femenino'), ('M', 'Masculino')], default='F', max_length=1)),
                ('area_salud', models.CharField(max_length=20)),
                ('dias_trabajo', models.SmallIntegerField(default=6, verbose_name='Cantidad de dias trabajados')),
                ('dia_ingreso', models.DateField(auto_now_add=True, verbose_name='Inicio hora laboral')),
            ],
        ),
        migrations.DeleteModel(
            name='HorasMedicas',
        ),
        migrations.AlterModelOptions(
            name='pacientes',
            options={'ordering': ['pa_rut'], 'verbose_name': 'rut_paciente', 'verbose_name_plural': 'rut_pacientes'},
        ),
    ]
