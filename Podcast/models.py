from django.db import models

# Create your models here.
#Creo el modelo para los programas o podcast.
class Programa(models.Model):
    nombre = models.CharField(max_length=30)
    genero = models.CharField(max_length=30)
    idioma = models.CharField(max_length=30)
    productora = models.CharField(max_length=30)
    
    #Creo el str para formatear la salida.
    def __str__(self):
        return f'Podcast: {self.nombre} de la productora: {self.productora} de genero: {self.genero} en: {self.idioma}'