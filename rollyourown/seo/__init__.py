__authors__ = ["Will Hardy <django-seo@willhardy.com.au>"]

from .version import __version__
from rollyourown.seo.base import Metadata, Tag, KeywordTag, MetaTag, Raw, Literal, get_metadata, get_linked_metadata


default_app_config = 'rollyourown.seo.apps.SeoConfig'
