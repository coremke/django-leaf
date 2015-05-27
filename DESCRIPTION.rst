django-leaf
===========

django-leaf renders both "static" and database-backed templates based on the URL path.

Quick Start
-----------

1. Install the package from pypi:

    .. code-block:: bash

        pip install django-leaf

2. Add "leaf" and "mptt" to your INSTALLED_APPS:

    .. code-block:: python

        INSTALLED_APPS = (
            ...
            'leaf',
            'mptt',
        )

3. Add leaf urls to *the end* of your urlpatterns:

    .. code-block:: python

        url(r'^', include('leaf.urls')),
