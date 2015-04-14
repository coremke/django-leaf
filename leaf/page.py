import os

from django.http import Http404


def get_names(url):
    """Get a list of valid page names.

    Valid page names will be a list of two types:

    1. The full page name provided
    2. The full page name provided starting with `pages/`

    Page names can also be used as the folder name, so index.html files
    will also work.

    Example:

    If the url is ``/example/leaf/url/``, the following page names will
    be returned:

    1. example/leaf/url
    2. example/leaf/url/index
    3. pages/example/leaf/url
    4. pages/example/leaf/url/index

    :param str url: The page URL (without extension)
    :returns: A list of valid template names (without extension) to look for

    """
    pages = []

    if url.startswith('admin'):
        return []

    pages.append(url)
    pages.append(os.path.join(url, 'index'))
    pages.append(os.path.join('pages', url))
    pages.append(os.path.join('pages', url, 'index'))

    return [strip_trailing_slash(p) for p in pages]


def get_url(view):
    """Get the path from the url route.

    The path can also be passed in through a keyword argument, `url`.

    :returns: The URL path for the requested page.

    """
    if getattr(view, 'url', None):
        return view.url

    url = view.kwargs.get('url', None)
    if url is None:
        raise Http404("URL not provided as class argument or kwarg")

    if url in ("/", ""):
        return "/index"

    return url


def strip_trailing_slash(value):
    """Strip trailing slash if exists.

    :param str value: The value to strip trailing slash from.
    :returns: Path without a trailing slash

    """
    if value.endswith('/'):
        return value[:-1]

    return value
