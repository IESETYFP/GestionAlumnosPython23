# Generated by Django 4.2.2 on 2023-11-08 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumnado', '0012_alumno_condicion_alumno_turno'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumno',
            name='cantidad_asistencias',
            field=models.IntegerField(default=0),
        ),
    ]