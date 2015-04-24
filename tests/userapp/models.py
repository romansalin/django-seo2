# -*- coding: utf-8 -*-
from django.db import models
from django.core.urlresolvers import reverse


class Page(models.Model):
    title = models.CharField(max_length=255, default="", blank=True)
    type = models.CharField(max_length=50, default="", blank=True)
    content = models.TextField(default="", blank=True)

    def get_absolute_url(self):
        return reverse('userapp_page_detail', args=[self.type])

    def __unicode__(self):
        return self.title or self.content


class Product(models.Model):
    meta_description = models.TextField(default="")
    meta_keywords = models.CharField(max_length=255, default="")
    meta_title = models.CharField(max_length=255, default="")

    def get_absolute_url(self):
        return reverse('userapp_product_detail', args=[self.id])

    def __unicode__(self):
        return self.meta_title


class Category(models.Model):
    name = models.CharField(max_length=255, default="M Category Name")
    page_title = models.CharField(max_length=255, default="M Category Page Title")

    def get_absolute_url(self):
        return reverse('userapp_my_view', args=["abc"])


class NoPath(models.Model):
    pass


class Tag(models.Model):
    name = models.CharField(max_length=255, default="")

    def get_absolute_url(self):
        return reverse('userapp_tag', args=[self.name])

    def __unicode__(self):
        return self.name
