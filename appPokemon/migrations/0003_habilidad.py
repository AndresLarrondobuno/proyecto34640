# Generated by Django 4.1.3 on 2022-12-01 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appPokemon', '0002_entrenador_pokemon'),
    ]

    operations = [
        migrations.CreateModel(
            name='Habilidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('tipo', models.CharField(max_length=20)),
            ],
        ),
    ]
