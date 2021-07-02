from django import forms
from .models import Producto
class FormularioProducto(forms.ModelForm):
    #Campos del modelo
    class Meta:
        model = Producto
        fields = ('titulo', 'descripcion', 'categoria', 'precio')
