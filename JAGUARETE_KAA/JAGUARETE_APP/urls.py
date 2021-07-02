#Archivo que va a redireccionar a la aplicacion
#Responde a las funciones de views.py de la aplicacion 
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('index', views.index, name="index"),
    path('acerca-de', views.acercaDe, name="acerca-de"),
    path('carrito', views.carrito, name="carrito"),
    path('login', views.login, name="login"),
    path('registro', views.registro, name="registro"),
    path('resultado-busqueda', views.resultadoBusqueda, name="resultado-busqueda"),
    path('categoria/<str:nombre>', views.categoria, name="resultado-busqueda"),

    #   --  CRUD PRODUCTOS  --  #
    #Crear producto
    path('nuevo-producto', views.nuevoProducto, name="nuevo-producto"),
    #Un producto
    path('producto/<int:producto_id>', views.producto, name="producto"),
    #Lista de productos
    path('productos', views.productos, name="productos"),
    #Actualizar producto
    path('productos/<int:producto_id>/modificar', views.modificarProducto, name="modificar-producto"),
    #Eliminar producto
    path('productos/<int:producto_id>/eliminar', views.eliminarProducto, name="eliminar-producto")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)