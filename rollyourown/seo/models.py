#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import importlib

from django.conf import settings
from django import VERSION as DJANGO_VERSION


def setup():
    # Look for Metadata subclasses in appname/seo.py files
    for app in settings.INSTALLED_APPS:
        try:
            module_name = '%s.seo' % str(app)
            importlib.import_module(module_name)
        except ImportError:
            pass

    # if SEO_MODELS is defined, create a default Metadata class
    if hasattr(settings, 'SEO_MODELS'):
        importlib.import_module('rollyourown.seo.default')

    from rollyourown.seo.base import register_signals
    register_signals()

if DJANGO_VERSION[:2] < (1, 7):
    setup()
