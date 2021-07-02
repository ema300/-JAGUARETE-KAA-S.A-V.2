from .models import Categorias

def ctx_dict(req):
    return {
        'lista_categorias': Categorias.objects.all()
    }