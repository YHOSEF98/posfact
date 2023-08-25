from django.shortcuts import render
from .signals import actualizar_stock
from django.db.models import F

from .models import *
from django.urls import reverse_lazy
from .forms import *
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

# Create your views here.
class EntradaListView(ListView):
    model = EntradaInventario
    template_name = 'inventario/entradasinv.html'

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Entradas de inventario'
        context["create_url"] = reverse_lazy('add-inv')
        return context

class EntradainvCreateView(CreateView):
    model = EntradaInventario
    form_class = EntradasInvForm
    template_name = 'inventario/createformsinv.html'
    success_url = reverse_lazy('entradas-inv')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Crear entrada de producto'
        context["volver"] = reverse_lazy('entradas-inv')
        context["titlebtn"] = 'Añadir entrada'
        context["titlerror"] = 'Ha ocurrido un error al guardar la entrada'
        return context


class EntradainvUpdateView(UpdateView):
    model = EntradaInventario
    form_class = EntradasInvForm
    template_name = 'inventario/createformsinv.html'
    success_url = reverse_lazy('entradas-inv')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Editar entrada'
        context["volver"] = reverse_lazy('entradas-inv')
        context["titlebtn"] = 'Editar entrada'
        context["titlerror"] = 'Ha ocurrido un error al guardar la centrada'
        return context

    def form_valid(self, form):
        entrada = form.save(commit=False)
        entrada.save()

        # Calcular la diferencia entre la cantidad original y la nueva cantidad
        diferencia_cantidad = entrada.cantidad - form.initial['cantidad']

        # Actualizar el stock según el tipo de instancia (entrada o salida)
        if isinstance(entrada, EntradaInventario):
            entrada.producto.stock = F('stock') + diferencia_cantidad
        else:
            entrada.producto.stock = F('stock') - diferencia_cantidad

        entrada.producto.save()

        return super().form_valid(form)


class EntradasinvDeleteView(DeleteView):
    model = EntradaInventario
    template_name = 'productos/deleteforms.html'
    success_url = reverse_lazy('entradas-inv')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Eliminar entrada'
        context["subtitle"] = 'la centrada inventario'
        context["volver"] = reverse_lazy('categorias')
        context["titlebtn"] = 'Si, eliminar entrada'
        context["cancelar"] = reverse_lazy('entradas-inv')
        context["url_cancelar"] = reverse_lazy('entradas-inv')
        context["titlerror"] = 'Ha ocurrido un error al eliminar la entrada'
        return context

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        # Actualizar el stock antes de eliminar la entrada
        self.object.producto.stock -= self.object.cantidad
        self.object.producto.save()

        # Invocar el método delete heredado para eliminar la entrada
        return super().delete(request, *args, **kwargs)


class SalidasListView(ListView):
    model = SalidaInventario
    template_name = 'inventario/salidasinv.html'

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Salidas de inventario'
        context["create_url"] = reverse_lazy('out-inv')
        return context



class SalidainvCreateView(CreateView):
    model = SalidaInventario
    form_class = SalidasInvForm
    template_name = 'inventario/createformsinv.html'
    success_url = reverse_lazy('salidas-inv')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Crear salida de producto'
        context["volver"] = reverse_lazy('salidas-inv')
        context["titlebtn"] = 'Añadir salida'
        context["titlerror"] = 'Ha ocurrido un error al guardar la salida del producto'
        return context