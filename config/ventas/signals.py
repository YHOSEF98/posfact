from django.db.models.signals import post_save
from .models import *
from ventas.models import *

def actualizar_facturado(sender, instance, created, **kwargs):
    pedido = instance.pedido

    # Actualizar stock en caso de entrada
    if sender == pedido.id and created:
        pedido.facturado += instance.facturado

    pedido.save()

post_save.connect(actualizar_facturado, sender=pedido)