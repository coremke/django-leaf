from django.http import Http404
from django.shortcuts import redirect
from django.template import TemplateDoesNotExist
from django.template.loader import select_template
from django.views.generic import TemplateView

from . import page


class LeafTemplateView(TemplateView):

    """Render a page from the database or the filesystem."""

    def dispatch(self, request, *args, **kwargs):
        """Override default to check for pages with optional trailing slash.

        If the requested path does not have a trailing slash, and the response
        was a 404, try the request again with the trailing slash.

        """
        self.page = page.get_from_database(kwargs.get('leaf_url'))

        try:
            return super(LeafTemplateView, self).dispatch(request, *args, **kwargs)
        except Http404:
            if not self.request.path.endswith("/"):
                return redirect(self.request.path + "/")
            raise

    def get_context_data(self, **kwargs):
        """Add the page to the template context."""
        context = super(LeafTemplateView, self).get_context_data(**kwargs)
        context['page'] = self.page
        return context

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
        if self.page:
            return [self.page.template]
        else:
            template_names = [u"{0}.html".format(p) for p in page.get_names(page.get_url(self))]

            try:
                t = select_template(template_names)

                if hasattr(t, 'template'):
                    # For django >= 1.8
                    return [t.template.name]
                else:
                    # For django < 1.8
                    return [t.name]
            except (TemplateDoesNotExist, UnicodeEncodeError):
                raise Http404(u"Template could not found. Tried: {0}".format(", ".join(template_names)))
