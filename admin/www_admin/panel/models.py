from django.db import models

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


    class Meta:
        db_table = 'usuarios'
        db_table = 'NumPartes'