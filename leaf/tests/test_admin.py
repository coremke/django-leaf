import pytest

from model_mommy import mommy


@pytest.mark.django_db
def test_get_inline_classes():
    from leaf.admin import GenericPageInline, get_inline_classes
    node = mommy.make('leaf.PageNode', slug='test', template='example-page')
    mommy.make("leaf_test.PageClass", node=node)

    assert get_inline_classes(None) == []
    assert get_inline_classes(node) == [GenericPageInline]
