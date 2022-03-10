===========
django-seo2
===========

History
-------
This is a fork of django-seo2_ library, which is no longer maintained.
The intention of this repo is to make it work under Python 3.8 and Django 3.2 as we upgrade the client project.
Many thanks for `Nitin Kondiparthi`_ and `Yiqing Lan`_'s work to make that happen.

.. _django-seo2: https://github.com/romansalin/django-seo2
.. _Nitin Kondiparthi: https://www.linkedin.com/in/nitin-kondiparthi/
.. _Yiqing Lan: https://www.linkedin.com/in/yiqinglan/

Overview
--------
This is a set of powerful and flexible SEO tools for Django. It allows you
to associate metadata with:

* absolute paths
* model instances
* model classes
* views

Metadata can be edited in the Django Admin in a centralised place,
but also alongside any associated models.

This is however a framework, not an app. To use this library, you need to define
the metadata you want and add the output to your templates.
Everything else (retrieval, formatting, escaping, caching) is handled for you.
Therefore, you have complete control over the data you store.

As requirements change, it may become necessary to add new metadata fields.
Having the metadata definition confined to a single, short class means that it
is easy to update.

Requirements
------------

* Python (3.8)
* Django (3.2)

Installation
-------------

Use `pip` plus a `requirements.txt` file to install. For example:

.. code-block:: console

    git+https://somehashstring@github.com/PeriShipLLC/yqnk-django-seo.git@tagcommitnumber


Example
-------

Here is an example of a definition:

.. code:: python

    from djangoseo import seo

    class BasicMetadata(seo.Metadata):
        title = seo.Tag(max_length=68, head=True)
        keywords = seo.KeywordTag()
        description = seo.MetaTag(max_length=155)
        heading = seo.Tag(name="h1")
        subheading = seo.Tag(name="h2")
        extra = seo.Raw(head=True)

        # Adding some fields for facebook (opengraph)
        og_title = seo.MetaTag(name="og:title",
                               populate_from="title",
                               verbose_name="facebook title")
        og_description = seo.MetaTag(name="og:description",
                                     populate_from="description",
                                     verbose_name='facebook description')

As you can see it is very flexible, but there is much more than this simple example.

The full documentation can be read online at http://django-seo2.readthedocs.org/.


