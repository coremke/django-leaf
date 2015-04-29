from django import forms

from .models import PageNode, PAGE_MODEL_CLASSES


def template_choices():
    """List out the template names for the admin."""
    return [('', '---------')] + [(m.identifier, m._meta.verbose_name.title()) for m in PAGE_MODEL_CLASSES]


class PageAdminForm(forms.ModelForm):

    """Page admin form including template choices."""

    template = forms.TypedChoiceField(choices=template_choices(), required=False)

    class Meta:
        model = PageNode
        exclude = ('path',)

    def __init__(self, *args, **kwargs):
        super(PageAdminForm, self).__init__(*args, **kwargs)

        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            self.fields['template'].widget.attrs['disabled'] = True
