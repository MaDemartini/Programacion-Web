# Generated by Django 4.2.13 on 2024-06-26 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticiero', '0004_noticia_imagen2'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscripcion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=8)),
                ('duracion', models.CharField(max_length=50)),
                ('funciones', models.TextField()),
                ('caracteristicas', models.TextField()),
                ('compatibilidad', models.TextField()),
                ('soporte', models.TextField()),
            ],
        ),
    ]
