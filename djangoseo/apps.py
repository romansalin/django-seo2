from django.apps.config import AppConfig

from djangoseo.models import setup


class SeoConfig(AppConfig):
    name = 'djangoseo'

    def ready(self):
        setup()
