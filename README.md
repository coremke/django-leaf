# django-leaf

> Render django templates based on URL path.

[![Build Status](https://img.shields.io/travis/gsmke/django-leaf/master.svg?style=flat)](https://travis-ci.org/gsmke/django-leaf)
[![Latest Version](https://img.shields.io/pypi/v/django-leaf.svg?style=flat)](https://pypi.python.org/pypi/django-leaf/)

## Quick start

1. Install the package from pypi

    ```bash
    pip install django-leaf
    ```

2. Add "leaf" to your INSTALLED_APPS setting:

    ```python
    INSTALLED_APPS = (
        ...
        'leaf',
    )
    ```

3. Add leaf urls to *the end* of your urlpatterns:

    ```python
    url(r'^', include('leaf.urls')),
    ```

## Usage

If you want to render a template when a user goes to `/example/url/`, create one of the following files:

1. example/url.html
2. example/url/index.html
3. pages/example/url.html
4. pages/example/url/index.html

# TODO

1. Better documentation.
2. More tests.
3. More configuration options.
