# Generated by Django 5.1.3 on 2024-12-04 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actividad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=25)),
                ('fecha_inicio', models.DateField()),
                ('arancel', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Entradas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sector', models.CharField(max_length=25)),
                ('precio', models.IntegerField()),
                ('partido', models.CharField(max_length=30)),
                ('competicion', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Socio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=25)),
                ('apellido', models.CharField(max_length=25)),
                ('DNI', models.IntegerField()),
                ('fecha_nacimiento', models.DateField()),
                ('categoria_socio', models.CharField(max_length=30)),
                ('numero_socio', models.IntegerField()),
            ],
        ),
    ]