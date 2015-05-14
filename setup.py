#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from setuptools import setup, find_packages


def read_version():
    """
    Extracts the version number from the version.py file.
    """
    version_file = 'djangoseo/version.py'
    v_locals = {}
    exec(open(version_file).read(), globals(), v_locals)
    return v_locals['__version__']


setup(
    name="django-seo",
    version=read_version(),
    packages=find_packages(exclude=["docs*", "tests*"]),
    install_requires=['Django>=1.7'],
    author="Will Hardy",
    author_email="djangoseo@willhardy.com.au",
    description="A framework for managing SEO metadata in Django.",
    long_description=open('README.rst').read(),
    license="LICENSE",
    keywords="seo, django, framework",
    url="https://github.com/whyflyru/django-seo",
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
    test_suite='tests.runtests.runtests',
    test_requires=['coveralls', 'coverage', 'django-discover-runner']
)
