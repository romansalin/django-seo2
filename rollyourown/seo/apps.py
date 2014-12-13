from django.apps.config import AppConfig
from rollyourown.seo.models import setup


class SeoConfig(AppConfig):
    def ready(self):
        setup()
