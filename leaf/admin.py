from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from .forms import PageAdminForm
from .models import PageNode, PAGE_MODEL_CLASSES


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
        inline = getattr(m, 'admin_inline', GenericPageInline)

        if getattr(m, 'identifier', None) == obj.template:
            inline.model = m
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
