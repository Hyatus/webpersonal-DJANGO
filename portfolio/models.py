from tabnanny import verbose
from django.db import models

# Create your models here.
# Aquí se crearan clases enlazadas a la base de datos 

class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name="Titulo") # Campo de caracteres
    description = models.TextField(verbose_name="Descripción") # Campo de caracteres
    image = models.ImageField(verbose_name="Imagen",upload_to="projects") # Campo de imagen, upload_to creará una carpeta en el directorio media llamado projects
    created = models.DateTimeField(auto_now_add=True,verbose_name="Fecha de Creación") # Este campo se añadirá la hora automáticamente
    updated = models.DateTimeField(auto_now=True,verbose_name="Fecha de Actualización") # Se actualizará la fecha cuando lo modifiquemos 
    
    class Meta: # Añadir metadatos extendidos 
        verbose_name = "proyecto"
        verbose_name_plural = "proyectos" # Nombre en plural
        ordering = ["-created"] # Ordenar por fecha de creación de forma inversa 

    def __str__(self):
        return self.title # Par que nos devuelva el nombre del proyecto


        