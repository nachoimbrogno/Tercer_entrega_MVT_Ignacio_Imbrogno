from django.db import models
from django.contrib.auth.models import User
# Create your models here.

#Creo el modelo para utilizar el avatar
class InformacionExtra(models.Model):
    avatar = models.ImageField(upload_to='avatares', null=True, blank=True)
    descripcion = models.TextField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)