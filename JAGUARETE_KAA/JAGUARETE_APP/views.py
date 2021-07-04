
from django.http.response import HttpResponseRedirect
from django.urls import reverse
from .models import Producto
from .forms import FormularioProducto
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse #Para peticiones HTTP

# from django.contrib.auth.forms import  UserCreationForm # formulario de django por defauld
from .forms import UserRegisterForm # formulario de django sobreescrito
from django.contrib import messages


# Create your views here.
def acercaDe(req):
    return render(req, "acerca-de/acerca-de.html")

def carrito(req):
    return render(req, "carrito/carrito.html")

def index(req):
    productos = Producto.objects.all().order_by('-id')[:3]
    return render(req, "index/index.html", {
        "ultimos_productos": productos
    })

def login(req):
    return render(req, "login/login.html")

def registro(req):
    if req.method== 'POST': #utilizo los campos que fueron llenados en el formulario
       form = UserRegisterForm(req.POST) # para acceder a la info que ha sido enviada a traves de este form
       if form.is_valid(): # si el form se lleno correctamente
           form.save() #guardo el form creado
         username= form.cleaned_data['username'] # para acceder al campo username
         messages.success(req,f'Usuario {username} creado con exito') 
        #  return redirect('index')

    else:  #si es por GET
        form=UserRegisterForm()
    context= {'form':form}    

    return render(req, "registro/registro.html",context)

def resultadoBusqueda(req):
    if req.method == "GET":
        busqueda = req.GET
        productos = Producto.objects.filter(titulo__icontains=busqueda['search'])
    return render(req, "resultado-busqueda/resultado-busqueda.html", {
        "productos": productos
    })

def categoria(req, nombre):
    productos = Producto.objects.filter(categoria__nombre__icontains=nombre)
    return render(req, "categoria/categoria.html", {
        "productos": productos
    })

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