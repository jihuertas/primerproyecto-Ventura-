from django.db import models

# Create your models here.
class Autor (models.Model):
    nombre = models.CharField(max_length=60, verbose_name="Nombre")
    apellidos = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    dni = models.CharField(unique=True, max_length=9)
    bio = models.TextField(blank=True, verbose_name="Biografía")
    fecha_nacimiento = models.DateField(blank=True,null=True)
    
    class Meta:
        verbose_name = "Autor"
        verbose_name_plural = "Autores"
    
    def __str__(self):
        return f"{self.pk} - {self.nombre}"  

class Post(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name="posts")
    cuerpo = models.TextField()
    fpublicado = models.DateField()

    def __str__(self):
        return self.titulo  

