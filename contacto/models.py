from django.db import models

# Create your models here.

class Contacto(models.Model):
    nombre = models.CharField(max_length=20, null=False, blank=False)
    apellido = models.CharField(max_length=20, null=False, blank=False)
    email= models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.nombre
        