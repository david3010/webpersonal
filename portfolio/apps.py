from django.apps import AppConfig


# Configuracion extendida del admin para la traduccion del nombre de la app
class PortfolioConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'portfolio'
    verbose_name = 'Portafolio'
