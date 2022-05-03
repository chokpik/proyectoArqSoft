# Generated by Django 4.0.4 on 2022-05-03 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('apellidos', models.CharField(max_length=200)),
                ('edad', models.IntegerField(max_length=4)),
                ('direccion', models.CharField(max_length=200)),
                ('ciudad', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=20)),
                ('nombreContacto', models.CharField(max_length=200)),
                ('direccionContacto', models.CharField(max_length=200)),
                ('telefonoContacto', models.CharField(max_length=20)),
                ('parentescoContacto', models.CharField(max_length=10)),
                ('nombreMedicoTratante', models.CharField(max_length=200)),
                ('diagnostico', models.CharField(max_length=400)),
                ('fechaUltimaConsulta', models.DateTimeField(verbose_name='Fecha ultima consulta')),
                ('impresionPersonal', models.CharField(max_length=400)),
            ],
        ),
    ]