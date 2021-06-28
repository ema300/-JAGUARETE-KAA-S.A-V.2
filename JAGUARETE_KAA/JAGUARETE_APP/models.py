from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class Categorias(models.Model):
    nombre = models.CharField(max_length=40)
    descripcion = models.CharField(max_length=250)

    def __str__(self):
        return f"Descripcion {self.id}: {self.nombre}:\n{self.descripcion}\n\n"
class Producto(models.Model):
    titulo = models.CharField(max_length=30)
    imagen = models.ImageField()
    descripcion = models.CharField(max_length=250)
    precio = models.FloatField()
    categoria = ''

    def __str__(self):
        return f"Libro {self.id}:\nTitulo:{self.titulo}\nDescripcion: {self.descripcion}\nPrecio:{self.precio}"

class Carrito(models.Model):
    usuario = models.CharField(max_length=25)
    lista_productos = []
    total_carrito = models.FloatField()

    def __str__(self):
        return f"Usuario {self.id} -> {self.usuario}\nLista de productos: {self.lista_productos}\nTotal: {self.total_carrito}"

#Tras crear un modelo se debe ejecutar 
# manage.py makemigrations -> despliega sobre la base de datos
# manage.py migrate -> implementa los cambios

# CONTROL DESDE LA CONSOLA
# manage.py shell -> consola de django
#   from JAGUARETE_APP import Categorias
# categoria = Categoria(descripcion="Una descripcion")
# categoria.save() //se guarda en la bd (esto coloca una id al ejemplar)