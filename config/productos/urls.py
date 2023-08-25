from django.urls import path
from .views import *

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('categorias/', CategoryListView.as_view(), name='categorias'),
    path('categorias/add', CategoryCreateView.as_view(), name='add'),
    path('categorias/edit/<int:pk>/', CategoryUpdateView.as_view(), name='edit_category'),
    path('categorias/delete/<int:pk>/', CategoryDeleteView.as_view(), name='delete_category'),
    path('', ProductListView.as_view(), name='productos'),
    path('add/', ProductCreateView.as_view(), name='add_product'),
    path('edit/<int:pk>/', ProductUpdateView.as_view(), name='edit_product'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='delete_product'),
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)