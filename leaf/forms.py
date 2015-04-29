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
        """Disable the template field when modifying.

        This field should only be set when creating the page.

        """
        super(PageAdminForm, self).__init__(*args, **kwargs)

        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            self.fields['template'].widget.attrs['disabled'] = True

    def clean_template(self):
        """Ensure the field is not changed when saving.

        When setting the field to disabled, the browser will not
        post the selected value. Always make sure it is set here.

        """
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            return instance.template
        return self.cleaned_data.get('template', None)
