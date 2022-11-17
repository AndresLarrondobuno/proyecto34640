from django.db import models

class Familiar(models.Model):
    nombre= models.CharField(max_length=30, default="string")
    edad= models.IntegerField(default=1)
    fecha_de_nacimiento= models.DateField(default=1993-12-12)

    def __str__(self):
        return self.nombre

