from django.db import models
from .choices import sexos
from .choices import estado
# Create your models here.

class Pacientes(models.Model):
    id_paciente = models.AutoField(primary_key=True)
    pa_nombre = models.CharField(max_length=20)
    pa_apellido = models.CharField(max_length=30)
    pa_rut = models.IntegerField()
    pa_edad = models.IntegerField()
    sexo = models.CharField(max_length=1, choices=sexos, default='F')
    seguro =  models.CharField(max_length=20)
    fec_ingreso = models.DateField()
    
    def __str__(self):
        texto ="{0} ({1})"
        return texto.format(self.pa_nombre, self.pa_apellido, self.pa_rut, self.pa_edad, self.sexo, self.seguro, self.fec_ingreso)
    
    def nombre_completo(self):
        return "{}, {}" .format(self.pa_apellido, self.pa_nombre)

    def __str__(self):
        return self.nombre_completo()

    class Meta:
        verbose_name='Paciente'
        verbose_name_plural='Pacientes'
        db_table='Pacientes'
        ordering=['pa_nombre', '-pa_apellido']


class Medicos(models.Model):
    id_medico = models.AutoField(primary_key=True)
    me_nombre = models.CharField(max_length=20)
    me_apellido = models.CharField(max_length=30)
    me_rut = models.IntegerField()
    me_edad = models.IntegerField()
    sexo = models.CharField(max_length=1, choices=sexos, default='F')
    area_salud =  models.CharField(max_length=20)
   
    def __str__(self):
        texto ="{0} ({1})"
        return texto.format(self.me_nombre, self.me_apellido, self.me_rut, self.me_edad, self.sexo, self.area_salud, self.dias_trabajo,  self.dia_ingreso, self.dia_salida)
    
    def nombre_medico(self):
        return "{}, {}" .format(self.me_apellido, self.me_nombre)

    def __str__(self):
        return self.nombre_medico()

    class Meta:
        verbose_name='Medico'
        verbose_name_plural='Medicos'
        db_table='Medicos'
        ordering=['me_nombre', '-me_apellido']


class HorasMedicas(models.Model):
    id_horamedica = models.AutoField(primary_key=True)
    paciente=models.CharField(max_length=40)
    medico=models.CharField(max_length=40 )
    consulta = models.CharField(max_length=40)
    fec_consulta = models.DateField()
    estado = models.CharField(max_length=1, choices=estado, default='A')
