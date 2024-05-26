from django.urls import path, include
from aplication import views

# Create your views here.
urlpatterns = [
    path("", views.home, name="home"),
    path('registro/', views.registro, name="registro"),
    path('opiniones/', views.mostrar_opiniones, name="mostrar_opiniones"),
    path('about/', views.about, name="about"),
]