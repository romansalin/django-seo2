# -*- coding: UTF-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin
from userapp.admin import alternative_site

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^alt-admin/', include(alternative_site.urls)),
    url(r'^', include('userapp.urls')),
)
