# Generated by Django 4.2.2 on 2023-09-22 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('especialidad', '0002_delete_especialidad'),
    ]

    operations = [
        migrations.CreateModel(
            name='Especialidad',
            fields=[
                ('id_especialidad', models.AutoField(primary_key=True, serialize=False)),
                ('nombreEspecialidad', models.CharField(max_length=50)),
                ('disenioCurricular', models.CharField(max_length=20)),
                ('cantidadMaterias', models.CharField(max_length=3)),
            ],
        ),
    ]