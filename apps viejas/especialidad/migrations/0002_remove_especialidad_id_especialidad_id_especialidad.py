# Generated by Django 4.2.2 on 2023-09-21 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('especialidad', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='especialidad',
            name='id',
        ),
        migrations.AddField(
            model_name='especialidad',
            name='id_especialidad',
            field=models.AutoField(default=0, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
