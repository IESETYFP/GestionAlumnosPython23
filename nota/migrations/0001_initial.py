# Generated by Django 4.2.2 on 2023-09-14 00:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('alumnado', '0005_alumno_id_curso'),
        ('materias', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.CharField(max_length=3)),
                ('fechaNota', models.DateField()),
                ('instancia', models.CharField(max_length=30)),
                ('AnnioCursada', models.CharField(max_length=5)),
                ('id_alumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alumnado.alumno')),
                ('id_materia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='materias.materia')),
            ],
        ),
    ]
