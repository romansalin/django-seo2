from setuptools import setup, find_packages

VERSION = "2.0.0"


def read_file(filepath):
    with open(filepath) as f:
        return f.read()


setup(
    name="yqnk-django-seo",
    version=VERSION,
    description="A framework for managing SEO metadata in Django.",
    long_description=read_file('README.rst'),
    url="https://github.com/PeriShipLLC/yqnk-django-seo",
    author="Nitin Kondiparthi, Yiqing Lan",
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
        "Programming Language :: Python :: 3.8",
    ],
    test_suite="tests.runtests.runtests",
)
