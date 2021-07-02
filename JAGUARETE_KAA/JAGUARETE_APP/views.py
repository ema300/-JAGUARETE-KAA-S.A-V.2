from django.http.response import HttpResponseRedirect
from django.urls import reverse
from .models import Producto
from .forms import FormularioProducto
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse #Para peticiones HTTP

# Create your views here.
def acercaDe(req):
    return render(req, "acerca-de/acerca-de.html")

def carrito(req):
    return render(req, "carrito/carrito.html")

def index(req):
    productos = Producto.objects.all().order_by('-id')[:3]
    print(productos)
    return render(req, "index/index.html", {
        "ultimos_productos": productos
    })

def login(req):
    return render(req, "login/login.html")

def registro(req):
    return render(req, "registro/registro.html")

def resultadoBusqueda(req):
    return render(req, "resultado-busqueda/resultado-busqueda.html")

#   -- CRUD PRODUCTOS   --
#   
#
# Mostrar un producto
def producto(req, producto_id):
    producto = Producto.objects.get(id=producto_id)
    return render(req, "producto/producto.html", {
        'producto': producto
    })

# Listar los productos
def productos(req):
    lista_productos = Producto.objects.all()
    return render(req, "productos/productos.html", {
        'lista_productos': lista_productos
    })

# Crear (cargar) un nuevo producto
def nuevoProducto(req):
    if req.method == "POST":
        formulario = FormularioProducto(req.POST)
        if formulario.is_valid():#Lado del servidor
            formulario.save()
            print("---Se guardo un producto---")
            return HttpResponseRedirect(reverse("nuevo-producto"))
    else:
        formulario = FormularioProducto()
        print("-x-No se guardo un producto-x-")
        return render(req, "nuevo-producto/nuevo-producto.html", {
            "form_producto": formulario
        })
    return render(req, "nuevo-producto/nuevo-producto.html")

# Modificar un producto
def modificarProducto(req, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if req.method == "POST":
        formulario = FormularioProducto(req.POST, instance=producto)
        if formulario.is_valid():
            formulario.save()
            return render(req, "producto/producto.html", {
                'producto': producto
            })
    else:
        formulario = FormularioProducto(instance=producto)
        return render(req, "modificar-producto/modificar-producto.html", {
            'producto': producto,
            'form_producto': formulario
        })

# Eliminar un producto
def eliminarProducto(req, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    producto.delete()
    return render(req, "productos/productos.html", {
        'lista_productos': Producto.objects.all()
    })

#Pasar el contexto a travez de un diccionario como tercer parametro
#Se accede a las sesiones por medio de request.session["item"], los elementos de la sesion son un string

#Para trabajar con sesiones se debe usar manae.py migrate para crear la tabla de sesiones