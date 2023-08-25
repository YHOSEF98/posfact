from django.urls import path
from .views import *

urlpatterns = [
    path('', ClientListView.as_view(), name='clientes'),
    path('addclient/', ClientCreateView.as_view(), name='add_client'),
    path('editclient/<int:pk>/', ClientUpdateView.as_view(), name='edit_client'),
    path('deletclient/<int:pk>/', ClientDeleteView.as_view(), name='delet_client'),
]