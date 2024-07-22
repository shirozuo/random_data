from django.apps import AppConfig


# Configuration for the "generator" application
class GeneratorConfig(AppConfig):
    # Default field for auto-created primary keys
    default_auto_field = 'django.db.models.BigAutoField'
    # Name of the application
    name = 'generator'
