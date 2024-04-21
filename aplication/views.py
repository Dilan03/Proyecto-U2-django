from django.shortcuts import render, HttpResponse, redirect
from .models import Videojuego, Categoria, Opinion
from . import forms

def home(request):
    categoria= Categoria.objects.get(nombre="question")
    categoria_id = categoria.id
    videojuegos = Videojuego.objects.filter(categoria=categoria_id)
    return render(request, "aplication/home.html", {'categoria': categoria, 'videojuegos': videojuegos})

#Crear un formulario para mostrar
def registro(request):
    form = forms.FormUser()

    #print(request.method)
    if request.method == 'POST':
        form = forms.FormUser(request.POST)
        if form.is_valid():
            print("VALIDADO!")
            print("Nombre: ", form.cleaned_data['nombre'])
            print("Correo: ", form.cleaned_data['correo'])
            print("Opinion: ", form.cleaned_data['opinion'])
            print(form.cleaned_data['botcatcher'])
            opinion = Opinion.objects.get_or_create(nombre=form.cleaned_data['nombre'],
                                                     correo=form.cleaned_data['correo'], 
                                                     opinion=form.cleaned_data['opinion'])[0]
            opinion.save()


    return render(request, "aplication/registro.html", {'form' : form})

def mostrar_opiniones(request):
    opiniones = Opinion.objects.all()
    return render(request, "aplication/opiniones.html", {'opiniones': opiniones})