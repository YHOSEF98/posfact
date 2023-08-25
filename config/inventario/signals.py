from django.db.models.signals import post_save
from .models import *
from ventas.models import *

def actualizar_stock(sender, instance, created, **kwargs):
    producto = instance.producto

    # Actualizar stock en caso de entrada
    if sender == EntradaInventario and created:
        producto.stock += instance.cantidad

    # Actualizar stock en caso de salida
    if (sender == SalidaInventario or sender == pedido) and created:
        producto.stock -= instance.cantidad

    producto.save()

post_save.connect(actualizar_stock, sender=EntradaInventario)
post_save.connect(actualizar_stock, sender=SalidaInventario)
post_save.connect(actualizar_stock, sender=pedido)
