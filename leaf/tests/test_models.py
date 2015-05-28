import pytest

from model_mommy import mommy


@pytest.mark.django_db
def test_page_node_str():
    home = mommy.make("leaf.PageNode", slug="home")
    assert str(home) == "home"


@pytest.mark.django_db
def test_page_node_save():
    home = mommy.make("leaf.PageNode", slug="home")
    about = mommy.make("leaf.PageNode", slug="about", parent=home)
    about_us = mommy.make("leaf.PageNode", slug="us", parent=about)

    assert home.path == 'home'
    assert about.path == 'about'
    assert about_us.path == 'about/us'
