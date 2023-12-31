# Generated by Django 4.1.7 on 2023-05-13 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='redsocial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Titulo')),
                ('descripcion', models.TextField(verbose_name='Descripcion')),
                ('link', models.URLField(blank=True, null=True, verbose_name='Direccion Web')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha Creacion')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha Actualizacion')),
            ],
            options={
                'verbose_name': 'Proyecto',
                'verbose_name_plural': 'Proyectos',
                'ordering': ['-created'],
            },
        ),
    ]
