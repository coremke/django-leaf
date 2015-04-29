# django-leaf

> Render django templates based on URL path.

[![Build Status](https://img.shields.io/travis/gsmke/django-leaf/master.svg?style=flat)](https://travis-ci.org/gsmke/django-leaf)
[![Latest Version](https://img.shields.io/pypi/v/django-leaf.svg?style=flat)](https://pypi.python.org/pypi/django-leaf/)

## Quick start

1. Install the package from pypi:

    ```bash
    pip install django-leaf
    ```

2. Add "leaf" and "mptt" to your INSTALLED_APPS:

    ```python
    INSTALLED_APPS = (
        ...
        'leaf',
        'mptt',
    )
    ```

3. Add leaf urls to *the end* of your urlpatterns:

    ```python
    url(r'^', include('leaf.urls')),
    ```

## Usage

django-leaf can be used to render both "static" and database-backed templates.

### Static Templates

If you want to render a template when a user goes to `/example/url/`, create one of the following files:

1. example/url.html
2. example/url/index.html
3. pages/example/url.html
4. pages/example/url/index.html

### Database Backed Templates

After installing django-leaf, the admin interface will have a new section called `Pages` where you'll be able to create your page hierarchy.

To define your own page model, you need to extend from `leaf.models.Page`.
There are a few fields available for customization:

1. **identifier**: A unique identifier for your model. This will be used to associate page nodes with your page implementation. If you don't provide an `identifier`, one will be provided for you.
2. **template**: The template to render.
3. **admin_inline**: The admin class to use when rendering the template fields inline. This defaults to the default ``admin.StackedInline``.

Here's an example for creating a page with translations provided by [django-parler](https://github.com/edoburu/django-parler):

```python
# admin.py
from parler.admin import TranslatableStackedInline


class AboutPageInline(TranslatableStackedInline):
    pass

# models.py
from django.db import models
from leaf.models import Page
from parler.models import TranslatableModel, TranslatedFields

from .admin import AboutPageInline


class AboutPage(Page, TranslatableModel):
    admin_inline = AboutPageInline
    identifier = 'about-page'
    template = "about.html"

    translations = TranslatedFields(
        headline=models.CharField(max_length=255),
        copy=models.TextField(blank=True)
    )

    def __unicode__(self):
        return self.headline
```

When rendering the template, all of the model fields will be available on the ``page`` context variable:

```django
{{ page.headline }}
{{ page.copy }}
```

# TODO

1. Better documentation.
2. More configuration options.
