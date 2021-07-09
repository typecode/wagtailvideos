from tests.app.settings import *  # noqa: F401,F403


ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'tests.sqlite3',
    },
}

INSTALLED_APPS += [
    'wagtail.contrib.styleguide',
]

WAGTAILVIDEOS_VIDEO_MODEL = 'app.CustomVideoModel'
WAGTAIL_USAGE_COUNT_ENABLED = True

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
