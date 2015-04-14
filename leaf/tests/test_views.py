import os
import tempfile


def test_view(client):
    t = tempfile.NamedTemporaryFile(suffix='.html')
    url_path = '/{}/'.format(os.path.basename(t.name.split('.html')[0]))
    resp = client.get(url_path)
    assert resp.status_code == 200


def test_view_redirect_with_slash(client):
    t = tempfile.NamedTemporaryFile(suffix='.html')
    url_path = '/{}123'.format(os.path.basename(t.name.split('.html')[0]))
    resp = client.get(url_path)
    assert resp.status_code == 302
    assert resp['location'].endswith(url_path + '/')


def test_view_404(client):
    resp = client.get('/test/testing/')
    assert resp.status_code == 404
