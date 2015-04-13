import os

from django.http import Http404
from django.shortcuts import redirect
from django.template import TemplateDoesNotExist
from django.template.loader import select_template
from django.views.generic import TemplateView


class LeafTemplateView(TemplateView):
    def _get_url(self):
        """Get the path from the url route.

        The path can also be passed in through a keyword argument, `url`.

        :returns: The URL path for the requested page.

        """
        if getattr(self, 'url', None):
            return self.url

        url = self.kwargs.get('url', None)
        if url is None:
            raise Http404("URL not provided as class argument or kwarg")

        if url in ("/", ""):
            return "index"

        return url

    def _strip_trailing_slash(self, value):
        """Strips trailing slash if exists."""
        if value.endswith('/'):
            return value[:-1]

        return value

    def _get_page_names(self):
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

        """
        pages = []

        page = self._get_url()
        if page.startswith('admin'):
            return []

        pages.append(page)
        pages.append(os.path.join(page, 'index'))
        pages.append(os.path.join('pages', page))
        pages.append(os.path.join('pages', page, 'index'))

        return [self._strip_trailing_slash(p) for p in pages]

    def dispatch(self, request, *args, **kwargs):
        """Override default to check for pages with optional trailing slash.

        If the requested path does not have a trailing slash, and the response
        was a 404, try the request again with the trailing slash.

        """
        try:
            response = super(LeafTemplateView, self).dispatch(request, *args, **kwargs)
            return response
        except Http404:
            if not self.request.path.endswith("/"):
                return redirect(self.request.path + "/")
            raise

    def get_template_names(self):
        """Get the template name that should be used for this page.

        This will use `get_page_names()` to find a list of valid template names
        that could be used for the page. It will then return the first one
        that is found.

        Note: This method will append ".html" to the page names returned by
        `get_page_names()`.

        Example:

        If you have a url as ``/example/leaf/url/``, the following templates
        will be tried:

        1. example/leaf/url.html
        2. example/leaf/url/index.html
        3. pages/example/leaf/url.html
        4. pages/example/leaf/url/index.html

        """
        template_names = [u"{0}.html".format(p) for p in self._get_page_names()]

        try:
            t = select_template(template_names)

            return [t.template.name]
        except (TemplateDoesNotExist, UnicodeEncodeError):
            raise Http404(u"Template could not found. Tried: {0}".format(", ".join(template_names)))
