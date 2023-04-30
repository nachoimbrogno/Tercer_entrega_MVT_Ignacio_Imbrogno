# Generated by Django 4.2 on 2023-04-29 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Programa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('genero', models.CharField(max_length=30)),
                ('idioma', models.CharField(max_length=30)),
                ('fecha_lanzamiento', models.DateField()),
                ('productora', models.CharField(max_length=30)),
                ('descripcion', models.TextField()),
            ],
        ),
    ]
