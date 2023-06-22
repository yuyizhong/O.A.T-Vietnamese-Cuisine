from django.apps import AppConfig
import os

if os.path.exists("env.py"):
    import env


class HomeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'home'
