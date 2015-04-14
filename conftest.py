import tempfile

from django.conf import settings


def pytest_configure():

    settings.configure(
        DEBUG=True,
        DATABASES={
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
            }
        },
        ROOT_URLCONF='leaf.urls',
        INSTALLED_APPS=(
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.admin',
            'leaf',
        ),
        TEMPLATE_DIRS=(
            tempfile.gettempdir(),
        )
    )
