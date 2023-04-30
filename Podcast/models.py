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
        #Lo uestro asi para que aparezca asi al consultar el podcast
        return f'{self.nombre} -- {self.productora} '