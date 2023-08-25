from django.db import models
from .choices import *

# Create your models here.
class Client(models.Model):
    names = models.CharField(max_length=150, verbose_name='Nombre', unique=True)
    surnames = models.CharField(max_length=150, verbose_name='Apellidos', unique=True)
    dni = models.CharField(max_length=10, unique=True, verbose_name='Documento')
    address = models.CharField(max_length=150, verbose_name='Direccion', null=True)
    sexo = models.CharField(max_length=10, choices=gender_choices, default='O', verbose_name='Sexo')
    
    def __str__(self):
        return self.names

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['id']