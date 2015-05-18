import os
import pytest

from model_mommy import mommy


@pytest.mark.parametrize('value', (
    '',
    '/',
    '/test/test2',
    '/test/test2/',
))
def test_strip_trailing_slash(value):
    from leaf.page import strip_trailing_slash
    assert not strip_trailing_slash(value).endswith('/')


@pytest.mark.parametrize('url', (
    '',
    'example',
    'example/test',
    'example/test/',
    'example/test2/test3',
))
def test_get_names(url):
    from leaf.page import get_names

    valid_paths = [
        url,
        os.path.join(url, 'index'),
        os.path.join('pages', url),
        os.path.join('pages', url, 'index'),
    ]

    return get_names(url) == valid_paths


@pytest.mark.parametrize('url', (
    'admin',
    'admin/',
    'admin/example',
    'admin/example/test',
    'admin/example/test/',
    'admin/example/test2/test3',
))
def test_get_names_admin(url):
    from leaf.page import get_names
    assert get_names(url) == []


@pytest.mark.parametrize('url,expected', (
    ('', '/index'),
    ('/', '/index'),
    ('/test', '/test'),
    ('/test/test2', '/test/test2'),
))
def test_get_url(url, expected):
    from leaf.page import get_url

    class View:
        kwargs = {
            'url': url
        }

    assert get_url(View()) == expected


def test_get_url_kwarg():
    from leaf.page import get_url

    class View:
        url = '/testing'

    assert get_url(View()) == '/testing'


def test_get_url_none():
    from django.http import Http404
    from leaf.page import get_url

    class View:
        kwargs = {
            'url': None
        }

    with pytest.raises(Http404):
        get_url(View())


@pytest.mark.django_db
def test_get_from_database():
    from leaf.page import get_from_database
    node = mommy.make('leaf.PageNode', slug='test', template='example-page')
    page_class = mommy.make("leaf_test.PageClass", node=node)

    assert get_from_database('test/') == page_class
    assert get_from_database('test') == page_class


@pytest.mark.django_db
def test_get_from_database_no_template():
    from leaf.page import get_from_database
    mommy.make('leaf.PageNode', slug='test')

    assert get_from_database('test/') is None
    assert get_from_database('test') is None


@pytest.mark.django_db
def test_get_from_database_no_page_class():
    from leaf.page import get_from_database
    mommy.make('leaf.PageNode', slug='test', template='example-page')

    assert get_from_database('test/') is None
    assert get_from_database('test') is None


@pytest.mark.django_db
def test_get_from_database_home_page():
    from leaf.page import get_from_database
    home_page = mommy.make('leaf.PageNode', slug='home', template='example-page')
    page_class = mommy.make("leaf_test.PageClass", node=home_page)

    assert get_from_database('') == page_class
    assert get_from_database('/') == page_class
    assert get_from_database('home') == page_class
    assert get_from_database('home/') == page_class
