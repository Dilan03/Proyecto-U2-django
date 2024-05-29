from django.urls import path, include
from aplication import views
from .views import HomeView, AboutView

# Create your views here.
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('registro/', views.registro, name="registro"),
    path('opiniones/', views.mostrar_opiniones, name="mostrar_opiniones"),
    path('about/', AboutView.as_view(), name='about'),
    path('logout/', views.exit, name="exit"),
    path('login/', view=views.LoginView.as_view(), name="login"),
]