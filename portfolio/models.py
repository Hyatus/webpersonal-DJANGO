from django.db import models

# Create your models here.
# Aquí se crearan clases enlazadas a la base de datos 

class Project(models.Model):
    title = models.CharField(max_length=200) # Campo de caracteres
    description = models.TextField() # Campo de caracteres
    image = models.ImageField() # Campo de imagen 
    created = models.DateTimeField(auto_now_add=True) # Este campo se añadirá la hora automáticamente
    updated = models.DateTimeField(auto_now=True) # Se actualizará la fecha cuando lo modifiquemos 