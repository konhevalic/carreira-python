from galeria.models import Fotografia
from django.shortcuts import render, get_object_or_404


def index(request):
    dados = {
        1: {"nome": "Nebulosa de Carina", "legenda": "Nasa"}
    }

    fotografias = Fotografia.objects.all()
    return render(request, 'galeria/index.html', {"cards": dados})

def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'galeria/imagem.html', {"fotografia": fotografia})