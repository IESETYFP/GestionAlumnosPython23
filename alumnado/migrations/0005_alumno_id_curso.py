# Generated by Django 4.2.2 on 2023-09-13 23:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('curso', '0001_initial'),
        ('alumnado', '0004_delete_asistencia'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumno',
            name='id_curso',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='curso.curso'),
        ),
    ]
