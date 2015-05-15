import pytest

from model_mommy import mommy


def test_template_choices():
    from leaf.forms import template_choices

    assert template_choices() == [
        ('', '---------'),
        ('example-page', 'Page Class'),
        ('example-page2', 'Page Class2'),
        ('example-page3', 'Page Class3'),
    ]


def test_page_admin_form():
    from leaf.forms import PageAdminForm

    form = PageAdminForm()
    assert not form.fields['template'].widget.attrs.get('disabled')


@pytest.mark.django_db
def test_page_admin_form_with_instance():
    from leaf.forms import PageAdminForm
    instance = mommy.make('leaf.PageNode', slug='test', template='example-page')

    form = PageAdminForm(instance=instance)
    assert form.fields['template'].widget.attrs['disabled']


@pytest.mark.django_db
def test_page_admin_form_update():
    from leaf.forms import PageAdminForm
    instance = mommy.make('leaf.PageNode', slug='test', template='example-page')

    form = PageAdminForm(instance=instance, data={'slug': 'test2'})
    form.is_valid()
    assert form.instance.template == 'example-page'
