from django.apps.config import AppConfig
from django.db.models.signals import post_migrate

from rollyourown.seo.models import setup
from rollyourown.seo.base import migrate_handler


class SeoConfig(AppConfig):
    name = 'rollyourown.seo'

    def ready(self):
        post_migrate.connect(migrate_handler, sender=self,
                             dispatch_uid="rollyourown.seo.management.populate_metadata")
        setup()
