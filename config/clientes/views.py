from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import *
from .forms import *

# Create your views here.

class ClientListView(ListView):
    model = Client
    template_name = 'clientes/clientes.html'

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Listado de clientes'
        context["create_url"] = reverse_lazy('add_client')
        return context



class ClientCreateView(CreateView):
    model = Client
    form_class = clientForm
    template_name = 'productos/createforms.html'
    success_url = reverse_lazy('clientes')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Crear cliente'
        context["volver"] = reverse_lazy('clientes')
        context["titlebtn"] = 'Añadir cliente'
        context["titlerror"] = 'Ha ocurrido un error al guardar el cliente'
        return context



class ClientUpdateView(UpdateView):
    model = Client
    form_class = clientForm
    template_name = 'productos/createforms.html'
    success_url = reverse_lazy('clientes')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Editar cliente'
        context["volver"] = reverse_lazy('clientes')
        context["titlebtn"] = 'Editar cliente'
        context["titlerror"] = 'Ha ocurrido un error al guardar el cliente'
        return context



class ClientDeleteView(DeleteView):
    model = Client
    template_name = 'clientes/deletecforms.html'
    success_url = reverse_lazy('clientes')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Eliminar el cliente'
        context["subtitle"] = 'el cliente'
        context["volver"] = reverse_lazy('clientes')
        context["titlebtn"] = 'Si, eliminar cliente'
        context["cancelar"] = reverse_lazy('clientes')
        context["url_cancelar"] = reverse_lazy('clientes')
        context["titlerror"] = 'Ha ocurrido un error al eliminar el cliente'
        return context