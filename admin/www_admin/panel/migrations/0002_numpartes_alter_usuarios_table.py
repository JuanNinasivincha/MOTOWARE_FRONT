# Generated by Django 5.0.4 on 2024-05-05 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NumPartes',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('dientes', models.IntegerField()),
                ('aros', models.DecimalField(decimal_places=2, max_digits=10)),
                ('litros', models.DecimalField(decimal_places=2, max_digits=10)),
                ('numero_partes', models.IntegerField(unique=True)),
            ],
            options={
                'db_table': 'NumPartes',
            },
        ),
        migrations.AlterModelTable(
            name='usuarios',
            table=None,
        ),
    ]
