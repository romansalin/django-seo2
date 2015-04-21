__authors__ = ["Will Hardy <django-seo@willhardy.com.au>"]

from rollyourown import version
from rollyourown.seo.base import Metadata, Tag, KeywordTag, MetaTag, Raw, Literal, get_metadata, get_linked_metadata


__version__ = version

from django import VERSION as DJANGO_VERSION
if DJANGO_VERSION >= (1, 7):
    default_app_config = 'rollyourown.seo.apps.SeoConfig'
