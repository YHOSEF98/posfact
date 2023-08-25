from django.urls import path
from .views import *


urlpatterns = [
    path("entradas/", EntradaListView.as_view(), name='entradas-inv'),
    path("entradas/add", EntradainvCreateView.as_view(), name='add-inv'),
    path("entradas/edit/<int:pk>/", EntradainvUpdateView.as_view(), name='edit-inv'),
    path("entradas/delete/<int:pk>/", EntradasinvDeleteView.as_view(), name='delete-inv'),
    path("salidas/", SalidasListView.as_view(), name='salidas-inv'),
    path("salidas/add", SalidainvCreateView.as_view(), name='out-inv'),
]