# Generated by Django 4.2.2 on 2023-11-08 20:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('asistencia', '0003_alter_asistencia_condicion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='asistencia',
            name='cantidadA',
        ),
        migrations.RemoveField(
            model_name='asistencia',
            name='condicion',
        ),
        migrations.RemoveField(
            model_name='asistencia',
            name='evento',
        ),
        migrations.RemoveField(
            model_name='asistencia',
            name='fechaA',
        ),
        migrations.RemoveField(
            model_name='asistencia',
            name='reintegrado',
        ),
        migrations.RemoveField(
            model_name='asistencia',
            name='turno',
        ),
    ]
