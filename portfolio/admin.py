from django.contrib import admin
from .models import Project

# Register your models here.


# Configuracion de extension de configuracion para registro de la app en el admin y extender la configuracion de los campos que se muestran del modelo
class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


admin.site.register(Project, ProjectAdmin)
