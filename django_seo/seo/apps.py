from django.apps.config import AppConfig

from django_seo.seo.models import setup


class SeoConfig(AppConfig):
    name = 'django_seo.seo'

    def ready(self):
        setup()
