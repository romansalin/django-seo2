from __future__ import unicode_literals

import importlib

from django.conf import settings


def setup():
    is_loaded = False
    # Look for Metadata subclasses in appname/seo.py files
    for app in settings.INSTALLED_APPS:
        try:
            module_name = '%s.seo' % str(app)
            importlib.import_module(module_name)
            is_loaded = True
        except ImportError:
            pass

    # if SEO_MODELS is defined, create a default Metadata class
    if hasattr(settings, 'SEO_MODELS') and not is_loaded:
        importlib.import_module('djangoseo.default')

    from djangoseo.base import register_signals
    register_signals()
