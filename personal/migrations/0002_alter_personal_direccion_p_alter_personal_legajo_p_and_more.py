# Generated by Django 4.2.6 on 2023-11-04 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personal',
            name='direccion_p',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='personal',
            name='legajo_p',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='personal',
            name='rol_p',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='personal',
            name='telefono_p',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
