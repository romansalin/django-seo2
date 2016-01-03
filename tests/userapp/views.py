from __future__ import unicode_literals

from django.shortcuts import get_object_or_404, render, render_to_response

from userapp.models import Page, Tag, Product


def page_detail(request, page_type):
    page = get_object_or_404(Page, type=page_type)
    return render_to_response('object_detail.html', {'object': page})


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render_to_response('object_detail.html', {'object': product})


def tag_detail(request, tag_name):
    tag = get_object_or_404(Tag, name=tag_name)
    return render_to_response('object_detail.html', {'object': tag})


def my_view(request, text):
    context = {'text': text}
    return render(request, 'my_view.html', context)


def my_other_view(request, text):
    context = {'text': text}
    return render_to_response('my_view.html', context)
