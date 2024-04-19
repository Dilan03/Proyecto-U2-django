from django.shortcuts import render, HttpResponse
from .models import Videojuego, Categoria

def home(request):
    categoria= Categoria.objects.get(nombre="question")
    categoria_id = categoria.id
    videojuegos = Videojuego.objects.filter(categoria=categoria_id)
    return render(request, "aplication/home.html", {'categoria': categoria, 'videojuegos': videojuegos})