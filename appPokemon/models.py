from django.db import models

class Familiar(models.Model):
    nombre= models.CharField(max_length=30, default="string")
    edad= models.IntegerField(default=1)
    fecha_de_nacimiento= models.DateField(default=1993-12-12)

    def __str__(self):
        return self.nombre


class Pokemon(models.Model):
    nombre = models.CharField(max_length=20)
    tipo = models.CharField(max_length=20)
    nivel = models.IntegerField()


class Entrenador(models.Model):
    nombre = models.CharField(max_length=20)
    cantidad_de_medallas = models.IntegerField()
    region = models.CharField(max_length=20)


class Habilidad(models.Model):
    nombre = models.CharField(max_length=20)
    tipo = models.CharField(max_length=20)
    



    


