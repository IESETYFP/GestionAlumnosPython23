# Generated by Django 4.2.3 on 2023-07-13 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id_alumno', models.AutoField(primary_key=True, serialize=False)),
                ('dni_a', models.CharField(max_length=9)),
                ('cuil_a', models.CharField(max_length=15)),
                ('apellido_a', models.CharField(max_length=50)),
                ('nombre_a', models.CharField(max_length=50)),
                ('matricula', models.CharField(max_length=10)),
                ('tutores', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=20)),
                ('direccion', models.CharField(max_length=50)),
                ('fecha_nac', models.DateField()),
            ],
        ),
    ]
