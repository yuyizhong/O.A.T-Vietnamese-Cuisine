from django.apps import AppConfig
import os

if os.path.exists("env.py"):
    import env



class MenuConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'menu'
