from django.contrib import admin
from .models import Project
# Register your models here.
# .models hace referencia a la propia app

admin.site.register(Project)

