# Generated by Django 4.2.2 on 2023-09-23 19:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('materia', '0001_initial'),
        ('alumnado', '0005_alumno_id_curso'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notas',
            fields=[
                ('id_nota', models.AutoField(primary_key=True, serialize=False)),
                ('valor', models.CharField(max_length=3)),
                ('AnnioCursada', models.CharField(max_length=5)),
                ('instancia', models.CharField(max_length=30)),
                ('fechaNota', models.DateField()),
                ('id_alumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alumnado.alumno')),
                ('id_materia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='materia.materia')),
            ],
        ),
    ]
