import pytest

from model_mommy import mommy


def test_tempalte_choices():
    from leaf.forms import template_choices

    assert template_choices() == [
        ('', '---------'),
        ('example-page', 'Page Class'),
    ]


def test_page_admin_form():
    from leaf.forms import PageAdminForm

    form = PageAdminForm()
    assert not form.fields['template'].widget.attrs.get('disabled')


@pytest.mark.django_db
def test_page_admin_form_with_instance():
    from leaf.forms import PageAdminForm
    instance = mommy.make('leaf_test.PageClass')

    form = PageAdminForm(instance=instance)
    assert form.fields['template'].widget.attrs['disabled']
