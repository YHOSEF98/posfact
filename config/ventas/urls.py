from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.ventas, name='ventas'),
    path('add_venta/',views.add_ventas.as_view(), name='AddVenta'),
    path('export/', views.export_pdf_view, name="ExportPDF" ),
    path('add_venta2/',views.SaleCreateView.as_view(), name='Add2Venta'),
    path('pedidos/',views.PedidosListView.as_view(), name='pedidos'),
    path('pedidos/add/',views.PedidoCreateView.as_view(), name='addpedidos'),
    path('mesas/',views.MesasListView.as_view(), name='mesas'),
    path('mesas/add',views.MesaCreateView.as_view(), name='addmesa'),
    path('mesa/<int:mesa_id>/pedidos/', PedidosMesaListView.as_view(), name='lista-pedidos-mesa'),
]