from tests.app.settings import *  # noqa: F401,F403

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'tests.sqlite3',
    },
}

INSTALLED_APPS += [
    'wagtail.contrib.styleguide',
]
