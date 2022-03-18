# Generated by Django 3.2.9 on 2022-03-14 17:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_area', models.TextField(max_length=30, verbose_name='Area')),
            ],
        ),
        migrations.CreateModel(
            name='departamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_departamento', models.TextField(max_length=30, verbose_name='Departamento')),
                ('area', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='company.area')),
            ],
        ),
        migrations.CreateModel(
            name='empresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_empresa', models.TextField(max_length=30, verbose_name='Empresa')),
            ],
        ),
        migrations.CreateModel(
            name='oficina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_oficina', models.TextField(max_length=30, verbose_name='Oficina')),
                ('direccion', models.TextField(max_length=300, verbose_name='Direccion')),
            ],
        ),
        migrations.CreateModel(
            name='empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField(max_length=30, verbose_name='Nombre')),
                ('apellidos', models.TextField(max_length=30, verbose_name='Apellidos')),
                ('departamento', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='company.departamento')),
            ],
        ),
        migrations.AddField(
            model_name='area',
            name='empresa',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='company.empresa'),
        ),
    ]
