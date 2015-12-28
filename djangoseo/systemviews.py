from __future__ import unicode_literals

import importlib

from django.apps import apps


def get_seo_views(metadata_class):
    return get_view_names(metadata_class._meta.seo_views)


def get_view_names(seo_views):
    output = []
    for name in seo_views:
        try:
            app = apps.get_app_config(name).models_module
        except Exception:
            output.append(name)
        else:
            app_name = app.__name__.split(".")[:-1]
            app_name.append("urls")
            try:
                urls = importlib.import_module(".".join(app_name))
            except (ImportError, AttributeError):
                output.append(name)
            else:
                for url in urls.urlpatterns:
                    if getattr(url, 'name', None):
                        output.append(url.name)
    return output
