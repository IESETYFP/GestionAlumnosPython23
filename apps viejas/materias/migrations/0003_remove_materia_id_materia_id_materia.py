# Generated by Django 4.2.2 on 2023-09-21 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materias', '0002_materia_id_especialidad'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='materia',
            name='id',
        ),
        migrations.AddField(
            model_name='materia',
            name='id_materia',
            field=models.AutoField(default=0, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
