from django.db import models

# Create your models here.
#Creo el modelo para los programas o podcast.
class Programa(models.Model):
    nombre = models.CharField(max_length=30)
    genero = models.CharField(max_length=30)
    idioma = models.CharField(max_length=30)
    fecha_lanzamiento = models.DateField()
    productora = models.CharField(max_length=30)
    descripcion = models.TextField()
    
    #Creo el str para formatear la salida.
    def __str__(self):
        return f'El podcast: {self.nombre} de la productora: {self.productora} lanzado : {self.fecha}'