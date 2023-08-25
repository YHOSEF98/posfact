from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .forms import *


from .models import *

# Create your views here.
class CategoryListView(ListView):
    model = Category
    template_name = 'productos/category.html'

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Listado de categorias'
        context["create_url"] = reverse_lazy('add')
        return context
    
class CategoryCreateView(CreateView):
    model = Category
    form_class = categoryForm
    template_name = 'productos/createforms.html'
    success_url = reverse_lazy('categorias')

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
        context["title"] = 'Crear categoria'
        context["volver"] = reverse_lazy('categorias')
        context["titlebtn"] = 'Añadir categoria'
        context["titlerror"] = 'Ha ocurrido un error al guardar la categoría'
        context['action']= 'add'
        context['list_url'] = reverse_lazy('categorias')
        return context


class CategoryUpdateView(UpdateView):
    model = Category
    form_class = categoryForm
    template_name = 'productos/createforms.html'
    success_url = reverse_lazy('categorias')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Editar categoria'
        context["volver"] = reverse_lazy('categorias')
        context["titlebtn"] = 'Editar categoria'
        context["titlerror"] = 'Ha ocurrido un error al guardar la categoría'
        return context


class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'productos/deleteforms.html'
    success_url = reverse_lazy('categorias')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Eliminar categoria'
        context["subtitle"] = 'la categoria'
        context["volver"] = reverse_lazy('categorias')
        context["titlebtn"] = 'Si, eliminar categoria'
        context["cancelar"] = reverse_lazy('categorias')
        context["url_cancelar"] = reverse_lazy('categorias')
        context["titlerror"] = 'Ha ocurrido un error al eliminar la categoría'
        return context


class ProductListView(ListView):
    model = Product
    template_name = 'productos/product.html'

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Listado de productos'
        context["create_url"] = reverse_lazy('add_product')
        return context


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'productos/createforms.html'
    success_url = reverse_lazy('productos')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Crear Producto'
        context["volver"] = reverse_lazy('productos')
        context["titlebtn"] = 'Añadir Producto'
        context["titlerror"] = 'Ha ocurrido un error al guardar el producto'
        return context


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'productos/createforms.html'
    success_url = reverse_lazy('productos')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Editar producto'
        context["volver"] = reverse_lazy('productos')
        context["titlebtn"] = 'Editar producto'
        context["titlerror"] = 'Ha ocurrido un error al guardar el producto'
        return context


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'productos/deleteforms.html'
    success_url = reverse_lazy('productos')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Eliminar producto'
        context["subtitle"] = 'el producto'
        context["volver"] = reverse_lazy('productos')
        context["titlebtn"] = 'Si, eliminar producto'
        context["cancelar"] = reverse_lazy('productos')
        context["url_cancelar"] = reverse_lazy('productos')
        context["titlerror"] = 'Ha ocurrido un error al eliminar el producto'
        return context