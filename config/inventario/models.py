from django.db import models
from productos.models import Product

# Create your models here.
class EntradaInventario(models.Model):
    producto = models.ForeignKey(Product, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    fecha = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Entrada de {self.cantidad} {self.producto.nombre}"

class SalidaInventario(models.Model):
    producto = models.ForeignKey(Product, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    fecha = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Salida de {self.cantidad} {self.producto.nombre}"
