from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class Categorias(models.Model):
    nombre = models.CharField(max_length=40)
    descripcion = models.CharField(max_length=250)

    def __str__(self):
        return f"{self.nombre}\n"
class Producto(models.Model):
    titulo = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=512)
    categoria = models.ForeignKey(Categorias, on_delete=models.CASCADE, related_name="categoria", default="Tecnologia")
    precio = models.FloatField()
    imagen = models.ImageField(upload_to="images")

    def __str__(self):
        return f"{self.id}:\nTitulo:{self.titulo}\n--- {self.descripcion}\n---Precio:{self.precio}"

class Carrito(models.Model):
    usuario = models.CharField(max_length=25)
    lista_productos = []
    total_carrito = models.FloatField()

    def __str__(self):
        return f"Usuario {self.id} -> {self.usuario}\nLista de productos: {self.lista_productos}\nTotal: {self.total_carrito}"

class Usuario(models.Model):
    usuario = models.CharField(max_length=25)
    password = models.CharField(max_length=16)

    def __str__(self):
        return f"ID: {self.id}\tUsuario:{self.usuario}"
#Tras crear un modelo se debe ejecutar 
# manage.py makemigrations -> despliega sobre la base de datos
# manage.py migrate -> implementa los cambios

# CONTROL DESDE LA CONSOLA
# manage.py shell -> consola de django
#   from JAGUARETE_APP import Categorias
# categoria = Categoria(descripcion="Una descripcion")
# categoria.save() //se guarda en la bd (esto coloca una id al ejemplar)