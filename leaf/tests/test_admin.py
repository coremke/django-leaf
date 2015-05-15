import pytest

from model_mommy import mommy


@pytest.mark.django_db
def test_get_inline_classes_default():
    from leaf.admin import GenericPageInline, get_inline_classes
    node = mommy.make('leaf.PageNode', slug='test', template='example-page')
    mommy.make("leaf_test.PageClass", node=node)

    assert get_inline_classes(None) == []
    assert get_inline_classes(node) == [GenericPageInline]


@pytest.mark.django_db
def test_get_inline_classes_admin_inlines():
    from leaf.admin import get_inline_classes
    from leaf_test.models import TestPageInline, TestInline, TestInline2
    node = mommy.make('leaf.PageNode', slug='test', template='example-page2')
    mommy.make("leaf_test.PageClass2", node=node)

    assert get_inline_classes(node) == [TestPageInline, TestInline, TestInline2]


@pytest.mark.django_db
def test_get_inline_classes_updated_admin_page_inline():
    from leaf.admin import get_inline_classes
    from leaf_test.models import TestPageInline
    node = mommy.make('leaf.PageNode', slug='test', template='example-page3')
    mommy.make("leaf_test.PageClass3", node=node)

    assert get_inline_classes(node) == [TestPageInline]
