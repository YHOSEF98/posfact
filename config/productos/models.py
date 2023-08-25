from django.db import models
from django.forms import model_to_dict
from config.settings import MEDIA_URL, STATIC_URL


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre', unique=True)

    def __str__(self):
        return self.name

    def toJson(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['id']

class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre', unique=True)
    cate = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product/%Y/%m/%d', null=True, blank=True)
    pvp = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    stock = models.IntegerField(editable=False, default=0)
    costo= models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    cantidad = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now_add=True)
    descripcion = models,models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.name

    def get_image(self):
        if self.image:
            return '{}{}'.format(MEDIA_URL, self.image)
        return '{}{}'.format(STATIC_URL, 'img/empty.png')

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['id']