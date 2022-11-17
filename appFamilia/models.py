from django.db import models

class Familiar(models.Model):
    nombre = models.CharField(max_length=30)
    edad = models.IntegerField()
    fecha_de_nacimiento = models.DateField()

    def __repr__(self) -> str:
        return self.nombre

