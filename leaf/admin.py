import six

from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from .forms import PageAdminForm
from .models import PageNode, PAGE_MODEL_CLASSES

try:
    from django.utils.module_loading import import_string
except ImportError:
    from django.utils.module_loading import import_by_path as import_string


class GenericPageInline(admin.StackedInline):

    """Generic inline admin for leaf pages."""


def get_inline_classes(obj):
    """Get the proper inline classes for the current object.

    :param obj: The object to get inline classes for.

    """
    if not obj:
        return []

    inlines = []
    for m in PAGE_MODEL_CLASSES:
        # Get the page inline
        page_inline = getattr(m, 'admin_page_inline', GenericPageInline)
        if isinstance(page_inline, six.string_types):
            page_inline = import_string(page_inline)

        if getattr(m, 'identifier', None) == obj.template:
            page_inline.model = m
            inlines.append(page_inline)

            # Add other inlines if defined
            for inline in getattr(m, 'admin_inlines', []):
                if isinstance(inline, six.string_types):
                    inline = import_string(inline)
                inlines.append(inline)
    return inlines


class PageAdmin(MPTTModelAdmin):

    """Base leaf admin."""

    form = PageAdminForm

    class Media:
        css = {
            'all': ('leaf/css/admin.css',)
        }

    def get_inline_instances(self, request, obj=None):
        """Inject the template model fields in the admin."""
        return [i(self.model, self.admin_site) for i in get_inline_classes(obj)]

admin.site.register(PageNode, PageAdmin)
