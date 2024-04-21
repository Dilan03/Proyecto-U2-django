from django.db import models

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class Videojuego(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    desarrollador = models.CharField(max_length=100)
    fecha_lanzamiento = models.DateField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='videojuegos/', null=True, blank=True)

    def __str__(self):
        return self.titulo

class Opinion(models.Model):
    nombre = models.CharField(max_length=15)
    correo = models.EmailField(unique=True)
    opinion = models.CharField(max_length=100)

    def __str__(self):
        return self.opinion