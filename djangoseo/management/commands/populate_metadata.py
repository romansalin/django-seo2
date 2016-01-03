#!/usr/bin/env python
from __future__ import unicode_literals

import warnings

from django.core.management.base import BaseCommand, CommandError

from djangoseo.base import registry, populate_metadata


class Command(BaseCommand):
    help = "Populate the database with metadata instances for all models " \
           "listed in seo_models."

    @staticmethod
    def populate_all_metadata():
        """
        Create metadata instances for all models in seo_models if empty.

        Once you have created a single metadata instance, this will not run.
        This is because it is a potentially slow operation that need only be
        done once. If you want to ensure that everything is populated, run the
        populate_metadata management command.
        """
        for Metadata in registry.values():
            InstanceMetadata = Metadata._meta.get_model('modelinstance')
            if InstanceMetadata is not None:
                for model in Metadata._meta.seo_models:
                    populate_metadata(model, InstanceMetadata)

    def handle(self, *args, **options):
        warnings.warn("This is deprecated command. It's not necessary yet and "
                      "potentially slow.", DeprecationWarning, stacklevel=2)

        if len(args) > 0:
            raise CommandError("This command currently takes no arguments")

        self.populate_all_metadata()
