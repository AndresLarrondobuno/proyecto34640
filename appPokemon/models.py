from django.db import models

class Pokemon(models.Model):
    nombre = models.CharField(max_length=20)
    tipo = models.CharField(max_length=20)
    nivel = models.IntegerField()

    def __str__(self):
        return self.nombre


class Entrenador(models.Model):
    nombre = models.CharField(max_length=20)
    cantidad_de_medallas = models.IntegerField()
    region = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre
        

class Habilidad(models.Model):
    nombre = models.CharField(max_length=20)
    tipo = models.CharField(max_length=20)
 
    def __str__(self):
        return self.nombre   



    


