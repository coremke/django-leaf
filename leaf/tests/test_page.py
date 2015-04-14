import os
import pytest


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
