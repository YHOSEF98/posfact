from django.shortcuts import render
from .forms import *
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
from productos.models import Product
from clientes.models import Client
from .models import *
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.http import JsonResponse, HttpResponse
#from weasyprint.text.fonts import FontConfiguration
#from django.template.loader import get_template
#from weasyprint import HTML, CSS
#from django.conf import settings
#import os

# Create your views here.

def ventas(request):
    return render(request, 'ventas/ventas.html')


class SaleCreateView(LoginRequiredMixin, CreateView):
    model = Sale
    form_class = SaleForm
    template_name = 'ventas/addventas.html'
    success_url = reverse_lazy('ventas')
    url_redirect = success_url

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Creacion de Ventas'
        context["entity"] = 'Clientes'
        context["list_url"] = self.success_url
        return context

class add_ventas(ListView):
    template_name = 'ventas/add_ventas1.html'
    model = Egreso

    def dispatch(self,request,*args,**kwargs):
        return super().dispatch(request, *args, **kwargs)
    """
    def get_queryset(self):
        return ProductosPreventivo.objects.filter(
            preventivo=self.kwargs['id']
        )
    """
    def post(self, request,*ars, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'autocomplete':
                data = []
                for i in Product.objects.filter(descripcion__icontains=request.POST["term"])[0:10]:
                    item = i.toJSON()
                    item['value'] = i.descripcion
                    data.append(item)
            else:
                data['error'] = "Ha ocurrido un error"
        except Exception as e:
            data['error'] = str(e)

        return JsonResponse(data,safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["productos_lista"] = Product.objects.all()
        context["clientes_lista"] = Client.objects.all()
        context["title"] = 'creacion de ventas'
        context["staticidioma"]= "/clientes/index/js/idiom.json"
        return context



def export_pdf_view(request):
    print("ticket creado")

    return render(request)


class PedidosListView(ListView):
    model = pedido
    template_name = 'ventas/pedidos.html'

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Listado de Pedidos'
        context["create_url"] = reverse_lazy('addpedidos')
        return context


class PedidoCreateView(CreateView):
    model = pedido
    form_class = pedidoForm
    template_name = 'productos/createforms.html'
    success_url = reverse_lazy('pedidos')

    # def post(self, request, *args, **kwargs):
    #     data = {}
    #     try:
    #         action = request.POST['action']
    #         if action == 'add':
    #             form = self.get.form()
    #             if form.is_valid():
    #                 form.save()
    #             else:
    #                 data['error'] = form.errors
    #         else:
    #             data['error']= 'No ha ingresado a ninguna opcion'
    #     except Exception as e:
    #         data['error']=str(e)
    #     return JsonResponse(data)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Crear pedido'
        context["volver"] = reverse_lazy('pedidos')
        context["titlebtn"] = 'Añadir pedido'
        context["titlerror"] = 'Ha ocurrido un error al crear el pedido'
        context['action']= 'add'
        context['list_url'] = reverse_lazy('pedidos')
        return context


class MesasListView(ListView):
    model = Mesa
    template_name = 'ventas/mesas.html'

    # def post(self, request,*ars, **kwargs):
    #     data = {}
    #     try:
    #         action = request.POST['action']
    #         if action == 'autocomplete':
    #             data = []
    #             for i in Product.objects.filter(descripcion__icontains=request.POST["term"])[0:10]:
    #                 item = i.toJSON()
    #                 item['value'] = i.descripcion
    #                 data.append(item)
    #         else:
    #             data['error'] = "Ha ocurrido un error"
    #     except Exception as e:
    #         data['error'] = str(e)

    #     return JsonResponse(data,safe=False)
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Listado de cuentas en mesas'
        return context



class MesaCreateView(CreateView):
    model = Mesa
    form_class = MesaForm
    template_name = 'ventas/addmesa.html'
    success_url = reverse_lazy('mesas')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Crear mesa'
        context["volver"] = reverse_lazy('mesas')
        context["titlebtn"] = 'Añadir mesa'
        context["titlerror"] = 'Ha ocurrido un error al guardar la mesa'
        return context



class PedidosMesaListView(ListView):
    model = pedido
    template_name = 'ventas/pedidosmesa.html'  # Ajusta la ruta de la plantilla
    context_object_name = 'pedidos'

    def get_queryset(self):
        mesa_id = self.kwargs['mesa_id']  # Obtén el ID de la mesa desde la URL
        return pedido.objects.filter(mesa_id=mesa_id, facturado=False)  

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Detalle de la cuenta'
        context["create_url"] = reverse_lazy('addpedidos')
        return context