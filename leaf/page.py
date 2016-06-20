import os

from django.http import Http404

from .models import PAGE_MODEL_CLASSES, PageNode


def get_from_database(path):
    """Load a page from the database.

    :param path: The path
    :returns: The page object from the database if it exists,
              otherwise None

    """
    # Paths are stored without trailing slash in database,
    # so remove it if there is one
    if path.endswith('/'):
        path = path[:-1]

    if path == '':
        path = 'home'

    try:
        node = PageNode.objects.exclude(template='').get(path=path)
    except PageNode.DoesNotExist:
        return

    page_class = get_page_class(node.template)
    if page_class is None:
        return

    try:
        return page_class.objects.get(node=node)
    except page_class.DoesNotExist:
        return


def get_page_class(template):
    """Get the page class for the template defined in the database.

    :param str template: The template name.
    :returns: The class for the `template`, or None if it doesn't exist.

    """
    page_class = [p for p in PAGE_MODEL_CLASSES if p.identifier == template]
    if len(page_class) == 1:
        return page_class[0]


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

    url = view.kwargs.get('leaf_url', None)
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
