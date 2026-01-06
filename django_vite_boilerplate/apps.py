try:
    from django.apps import AppConfig
except ImportError:
    from types import NoneType

    AppConfig = NoneType


class ViteBoilerplateConfig(AppConfig):
    name = "django_vite_boilerplate"
    verbose_name = "Vite Boilerplate"
