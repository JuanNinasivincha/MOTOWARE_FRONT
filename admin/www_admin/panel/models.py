from django.db import models
from django.core.validators import MinValueValidator, EmailValidator
from django.utils import timezone

# Create your models here.


class Usuarios(models.Model):
    id = models.IntegerField(primary_key = True)
    nombre = models.CharField(max_length= 30, null=False)
    apellido = models.CharField(max_length= 30, null=False)
    correo = models.CharField(max_length= 30, null=False)
    telefono = models.IntegerField(null = False)
    fecha_nacimiento = models.DateField(null = True)
    fecha_registro = models.DateTimeField(auto_now_add = True, null = True)


class NumPartes(models.Model):
    id = models.AutoField(primary_key=True)
    dientes = models.IntegerField()
    aros = models.DecimalField(max_digits=10, decimal_places=2)
    litros = models.DecimalField(max_digits=10, decimal_places=2)
    numero_partes = models.IntegerField(unique=True)


class SolicitudRepuestos(models.Model):
    ESTADO_CHOICES = [
        ('aprobado', 'Aprobado'),
        ('denegado', 'Denegado'),
    ]

    id = models.AutoField(primary_key=True)
    usuario_mecanico = models.CharField(max_length=100, null=False)
    fecha_emision = models.DateTimeField(default=timezone.now)
    nombre_repuesto = models.CharField(max_length=100, null=False)
    cantidad_solicitada = models.PositiveIntegerField(validators=[MinValueValidator(1, message="La cantidad solicitada debe ser al menos 1")])
    descripcion_detalles = models.TextField(null=True, blank=True)
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES, default='aprobado')


    class Meta:
        db_table = 'usuarios'
        db_table = 'NumPartes'
        db_table = 'SolicitudRepuestoss'


