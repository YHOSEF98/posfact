from django.db import models
from datetime import datetime
from clientes.models import Client
from productos.models import Product
from .choices import *
from django.forms import model_to_dict
from django.urls import reverse

# Create your models here.
class Sale(models.Model):
    cli = models.ForeignKey(Client, on_delete=models.CASCADE)
    date_joined = models.DateField(default=datetime.now)
    subtotal = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    iva = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    total = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)

    def __str__(self):
        return self.cli.names

    class Meta:
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'
        ordering = ['id']


class Detsale(models.Model):
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE)
    prod = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    cant =  models.IntegerField(default=0)
    subtotal = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)

    def __str__(self):
        return self.prod.name

    class Meta:
        verbose_name = 'Detalle de venta'
        verbose_name_plural = 'Detalles de ventas'
        ordering = ['id']


class Egreso(models.Model):
    fecha_pedido = models.DateField(max_length=255)
    cliente = models.ForeignKey(Client, on_delete=models.SET_NULL , null=True , related_name='cliente')
    total = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    pagado = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    comentarios = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now=True)
    ticket = models.BooleanField(default=True)
    desglosar = models.BooleanField(default=True)
    updated = models.DateTimeField(auto_now_add=True , null=True)

    class Meta:
        verbose_name='egreso'
        verbose_name_plural = 'egresos'
        order_with_respect_to = 'fecha_pedido'
    
    def __str__(self):
        return str(self.id)


class ProductosEgreso(models.Model):
    egreso = models.ForeignKey(Egreso, on_delete=models.CASCADE)
    producto = models.ForeignKey(Product, on_delete=models.CASCADE)
    cantidad = models.DecimalField(max_digits=20, decimal_places=2 , null=False)
    precio = models.DecimalField(max_digits=20, decimal_places=2 , null=False , default=0)
    subtotal = models.DecimalField(max_digits=20, decimal_places=2 , null=False , default=0)
    iva = models.DecimalField(max_digits=20, decimal_places=2 , null=False , default=0)
    total = models.DecimalField(max_digits=20, decimal_places=2 , null=False , default=0)
    created = models.DateTimeField(auto_now_add=True)
    entregado = models.BooleanField(default=True)
    devolucion = models.BooleanField(default=False)

    class Meta:
        verbose_name='producto egreso'
        verbose_name_plural = 'productos egreso'
        order_with_respect_to = 'created'
    
    def __str__(self):
        return self.producto
    
    def toJSON(self):
        item = model_to_dict(self, exclude=['created'])
        return item


class Mesa(models.Model):
    cli= models.ForeignKey(Client, on_delete=models.CASCADE,blank=True, null=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    estado = models.CharField(max_length=10, choices=estadoMesa,default="L")

    class Meta:
        verbose_name='Mesa'
        verbose_name_plural = 'Mesas'
    
    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse('lista-pedidos-mesa', args=[str(self.id)])


class pedido(models.Model):
    mesa=models.ForeignKey(Mesa, on_delete=models.CASCADE,blank=True, null=True)
    producto=models.ForeignKey(Product, on_delete=models.CASCADE)
    cantidad=models.IntegerField()
    facturado = models.BooleanField(default=False)
    fecha = models.DateField(default=datetime.now)

    class Meta:
        verbose_name='Pedido'
        verbose_name_plural = 'Pedidos'
    
    def __str__(self):
        return self.producto
