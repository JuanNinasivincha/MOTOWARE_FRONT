# Generated by Django 5.0.4 on 2024-06-12 03:53

import django.core.validators
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0002_numpartes_alter_usuarios_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='SolicitudRepuestos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('usuario_mecanico', models.CharField(max_length=100)),
                ('fecha_emision', models.DateTimeField(default=django.utils.timezone.now)),
                ('nombre_repuesto', models.CharField(max_length=100)),
                ('cantidad_solicitada', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1, message='La cantidad solicitada debe ser al menos 1')])),
                ('descripcion_detalles', models.TextField(blank=True, null=True)),
                ('estado', models.CharField(choices=[('aprobado', 'Aprobado'), ('denegado', 'Denegado')], default='aprobado', max_length=10)),
            ],
            options={
                'db_table': 'SolicitudRepuestoss',
            },
        ),
        migrations.AlterModelTable(
            name='numpartes',
            table=None,
        ),
    ]
