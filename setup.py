from setuptools import setup, find_packages

VERSION = "1.0.1"


def read_file(filepath):
    with open(filepath) as f:
        return f.read()


setup(
    name="django-seo2",
    version=VERSION,
    description="A framework for managing SEO metadata in Django.",
    long_description=read_file('README.rst'),
    url="https://github.com/romansalin/django-seo2",
    author="Roman Salin",
    author_email="romansalin1990@gmail.com",
    keywords="seo django framework",
    license="MIT",
    include_package_data=True,
    zip_safe=False,
    packages=find_packages(exclude=["docs*", "tests*"]),
    install_requires=[],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Internet :: WWW/HTTP :: Indexing/Search",
        "Topic :: Internet :: WWW/HTTP :: Site Management",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
    ],
    test_suite="tests.runtests.runtests",
)
