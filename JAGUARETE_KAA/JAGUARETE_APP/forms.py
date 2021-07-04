from django import forms
from .models import Producto

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class FormularioProducto(forms.ModelForm):
    #Campos del modelo
    class Meta:
        model = Producto
        fields = ('titulo', 'descripcion', 'categoria', 'precio')

class UserRegisterForm(UserCreationForm):
    username= forms.CharField(label=' Usuario ')
    email = forms.EmailField()
    password1=forms.CharField(label=' Contraseña ',widget=forms.PasswordInput)
    password2=forms.CharField(label=' Confirmar Contraseña ',widget=forms.PasswordInput)


    
    class Meta:
        model=User # va estar asociada al usuario
        fields= ['username','email','password1','password2'] # campos que se veran en la vista del form
        help_texts = {k:"" for k in fields} #sobreescribo los textos por vacio