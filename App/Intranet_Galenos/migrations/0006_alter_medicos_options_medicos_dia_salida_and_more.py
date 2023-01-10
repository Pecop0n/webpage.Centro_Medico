# Generated by Django 4.0.5 on 2022-12-11 05:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Intranet_Galenos', '0005_alter_pacientes_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='medicos',
            options={'ordering': ['me_nombre', '-me_apellido'], 'verbose_name': 'Medico', 'verbose_name_plural': 'Medicos'},
        ),
        migrations.AddField(
            model_name='medicos',
            name='dia_salida',
            field=models.DateField(auto_now_add=True, verbose_name='Salida hora laboral'),
            preserve_default=False,
        ),
        migrations.AlterModelTable(
            name='medicos',
            table='Medicos',
        ),
        migrations.CreateModel(
            name='HorasMedicas',
            fields=[
                ('id_horamedica', models.IntegerField(primary_key=True, serialize=False)),
                ('consulta', models.CharField(max_length=40)),
                ('estado', models.CharField(choices=[('A', 'Antendido'), ('P', 'Pendeinte')], default='A', max_length=1)),
                ('medico', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Intranet_Galenos.medicos')),
                ('paciente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Intranet_Galenos.pacientes')),
            ],
        ),
    ]