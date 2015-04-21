#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from setuptools import setup, find_packages

setup(
    name="DjangoSEO",
    version='1.0',
    packages=find_packages(exclude=["docs*", "tests*"]),
    namespace_packages=['rollyourown'],
    install_requires=['Django>=1.6'],
    author="Will Hardy",
    author_email="djangoseo@willhardy.com.au",
    description="A framework for managing SEO metadata in Django.",
    long_description=open('README.rst').read(),
    license="LICENSE",
    keywords="seo, django, framework",
    url="https://github.com/willhardy/django-seo",
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "License :: OSI Approved :: Apache Software License",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Topic :: Software Development"
    ],
    test_suite='tests.runtests.runtests'
)
