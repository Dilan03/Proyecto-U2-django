import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'meats.settings')
import django
django.setup()

import random
from faker import Faker
from aplication.models import Categoria, Videojuego

fake = Faker()

# Función para poblar la tabla de Categoría
def populate_categorias(n):
    for _ in range(n):
        nombre = fake.word()
        descripcion = fake.text()
        Categoria.objects.create(nombre=nombre, descripcion=descripcion)

# Función para poblar la tabla de Videojuego
def populate_videojuegos(n):
    categorias = Categoria.objects.all()
    for _ in range(n):
        titulo = fake.company()
        descripcion = fake.text()
        desarrollador = fake.name()
        fecha_lanzamiento = fake.date_between(start_date='-10y', end_date='today')
        precio = round(random.uniform(10, 60), 2)
        categoria = random.choice(categorias)
        imagen = None  # Puedes agregar la lógica para cargar imágenes aquí
        Videojuego.objects.create(titulo=titulo, descripcion=descripcion, desarrollador=desarrollador,
                                   fecha_lanzamiento=fecha_lanzamiento, precio=precio, categoria=categoria,
                                   imagen=imagen)

if __name__ == '__main__':
    num_categorias = 5  # Número de categorías a crear
    num_videojuegos = 20  # Número de videojuegos a crear

    print("Creando categorías...")
    populate_categorias(num_categorias)
    print("Categorías creadas con éxito.")

    print("Creando videojuegos...")
    populate_videojuegos(num_videojuegos)
    print("Videojuegos creados con éxito.")
