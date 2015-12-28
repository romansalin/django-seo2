from __future__ import unicode_literals

from django.contrib import admin
from djangoseo.admin import (register_seo_admin, get_inline,
                             auto_register_inlines)

from userapp.seo import Coverage, WithSites, WithSEOModels
from userapp.models import Product, Page, Category, Tag, NoPath


class WithMetadataAdmin(admin.ModelAdmin):
    inlines = [get_inline(Coverage), get_inline(WithSites)]


register_seo_admin(admin.site, Coverage)
register_seo_admin(admin.site, WithSites)

try:
    admin.site.register(Product, admin.ModelAdmin)
except admin.sites.AlreadyRegistered:
    pass
try:
    admin.site.register(Page, admin.ModelAdmin)
except admin.sites.AlreadyRegistered:
    pass
try:
    admin.site.register(Tag, WithMetadataAdmin)
except admin.sites.AlreadyRegistered:
    pass
try:
    admin.site.register(NoPath, WithMetadataAdmin)
except admin.sites.AlreadyRegistered:
    pass

# Register alternative site here to avoid double import
alternative_site = admin.AdminSite()
alternative_site.register(Tag)
auto_register_inlines(alternative_site, Coverage)
alternative_site.register(Page)
auto_register_inlines(alternative_site, WithSites)
auto_register_inlines(alternative_site, WithSEOModels)
alternative_site.register(Product)
