from django.shortcuts import render, HttpResponse, redirect
from .models import Videojuego, Categoria, Opinion
from . import forms
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = "aplication/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categoria = Categoria.objects.get(nombre="question")
        context['categoria'] = categoria
        context['videojuegos'] = Videojuego.objects.filter(categoria=categoria.id)
        context['imagen'] = Videojuego.objects.filter(categoria=categoria.id).first().imagen.url
        return context

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

class AboutView(TemplateView):
    template_name = "aplication/about.html"

class LoginView(TemplateView):
    template_name = "aplication/registration/login.html"

@login_required
def mostrar_opiniones(request):
    opiniones = Opinion.objects.all()
    return render(request, "aplication/opiniones.html", {'opiniones': opiniones})

def exit(request):
    logout(request)
    return redirect('home')