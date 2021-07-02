from django.contrib import admin
from .models import Producto, Categorias, Carrito

# Register your models here.
#admin.site.register(Producto)
admin.site.register(Categorias)
admin.site.register(Producto)
admin.site.register(Carrito)