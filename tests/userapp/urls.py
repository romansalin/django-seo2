from __future__ import unicode_literals

from django.conf.urls import url

from userapp import views

urlpatterns = [
    url(r'^pages/([\w\d-]+)/', views.page_detail, name="userapp_page_detail"),
    url(r'^products/(\d+)/', views.product_detail,
        name="userapp_product_detail"),
    url(r'^tags/(.+)/', views.tag_detail, name="userapp_tag"),
    url(r'^my/view/(.+)/', views.my_view, name="userapp_my_view"),
    url(r'^my/other/view/(.+)/', views.my_other_view,
        name="userapp_my_other_view"),
]
