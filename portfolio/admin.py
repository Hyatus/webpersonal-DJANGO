from django.contrib import admin
from .models import Project
# Register your models here.
# .models hace referencia a la propia app



class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated') # Muestra campos que serán sólo de lectura la fecha de creación y actualización


admin.site.register(Project,ProjectAdmin) # Agregamos las configuraciones extendidas 

