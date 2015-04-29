import os
import six
import tempfile

if six.PY3:
    from unittest import mock
else:
    import mock


class DatabasePage():
    pass


def test_view_fs(client):
    with mock.patch('leaf.page.get_from_database', return_value=None):
        t = tempfile.NamedTemporaryFile(suffix='.html')
        url_path = '/{}/'.format(os.path.basename(t.name.split('.html')[0]))
        resp = client.get(url_path)
        assert resp.status_code == 200
        assert resp.context['page'] is None


def test_view_fs_redirect_with_slash(client):
    with mock.patch('leaf.page.get_from_database', return_value=None):
        t = tempfile.NamedTemporaryFile(suffix='.html')
        url_path = '/{}123'.format(os.path.basename(t.name.split('.html')[0]))
        resp = client.get(url_path)
        assert resp.status_code == 302
        assert resp['location'].endswith(url_path + '/')


def test_view_fs_404(client):
    with mock.patch('leaf.page.get_from_database', return_value=None):
        resp = client.get('/test/testing/')
        assert resp.status_code == 404


def test_view_db(client):
    t = tempfile.NamedTemporaryFile(suffix='.html')
    page = DatabasePage()
    page.template = t.name

    with mock.patch('leaf.page.get_from_database', return_value=page):
        url_path = '/{}/'.format(os.path.basename(t.name.split('.html')[0]))
        resp = client.get(url_path)
        assert resp.status_code == 200
        assert resp.context['page'] == page


def test_view_db_redirect_with_slash(client):
    t = tempfile.NamedTemporaryFile(suffix='.html')
    page = DatabasePage()
    page.template = t.name

    with mock.patch('leaf.page.get_from_database', return_value=page):
        url_path = '/{}123'.format(os.path.basename(t.name.split('.html')[0]))
        resp = client.get(url_path)
        assert resp.status_code == 200
        assert resp.context['page'] == page
