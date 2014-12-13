#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import django

def setup():
    from django.conf import settings

    # Look for Metadata subclasses in appname/seo.py files
    for app in settings.INSTALLED_APPS:
        try:
            module_name = '%s.seo' % str(app)
            __import__(module_name)
        except ImportError:
            pass

    # if SEO_MODELS is defined, create a default Metadata class
    if hasattr(settings, 'SEO_MODELS'):
        __import__('rollyourown.seo.default')

    from rollyourown.seo.base import register_signals
    register_signals()

if django.VERSION[:2] < (1, 7):
    setup()
