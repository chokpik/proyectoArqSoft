from django.db import models
from django.utils import timezone

class Paciente(models.Model):
    nombre = models.CharField(max_length=200)
    apellidos = models.CharField(max_length=200)
    edad = models.IntegerField()
    direccion = models.CharField(max_length=200)
    ciudad = models.CharField(max_length=50)
    telefono = models.CharField(max_length=20)
    nombreContacto = models.CharField(max_length=200)
    direccionContacto = models.CharField(max_length=200)
    telefonoContacto = models.CharField(max_length=20)
    parentescoContacto = models.CharField(max_length=10)
    nombreMedicoTratante = models.CharField(max_length=200)
    diagnostico = models.CharField(max_length=400)
    fechaUltimaConsulta = models.DateTimeField("Fecha ultima consulta")
    impresionPersonal = models.CharField(max_length=400)

    def __str__(self):
        return "nombre: " + self.nombre + " apellidos: " + self.apellidos + " telefono: " + self.telefono



