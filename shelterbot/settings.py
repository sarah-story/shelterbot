# Django settings for shelterbot project.

import os
import dj_database_url

# The top directory for this project. Contains requirements/, manage.py,
# and README.rst, a shelterbot directory with settings etc (see
# PROJECT_PATH), as well as a directory for each Django app added to this
# project.
PROJECT_ROOT = os.path.dirname(os.path.dirname(__file__))

# The directory with this project's templates, settings, urls, static dir,
# wsgi.py, fixtures, etc.
PROJECT_PATH = os.path.join(PROJECT_ROOT, 'shelterbot')

DEBUG = True
TEMPLATE_DEBUG = DEBUG

# Default Response

DEFAULT_RESPONSE = "Hi, this is ShelterBot! Text me what you need!"

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'shelterbot.db',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/public/media/"
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'public', 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/public/static/"
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'public', 'static')

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files to collect
STATICFILES_DIRS = (
    os.path.join(PROJECT_PATH, 'static'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Make this unique, and don't share it with anybody.
SECRET_KEY = '09+b1q6veb)q=1)fdwd#h!^-#&(uc!0xd+lw^+nvii=jurbze_'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
)

MIDDLEWARE_CLASSES = (
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ALLOWED_HOSTS = ["shelter-bot.herokuapp.com", "shelter-bot-dev.herokuapp.com", "localhost", "127.0.0.1"]

ROOT_URLCONF = 'shelterbot.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'shelterbot.wsgi.application'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_PATH, 'templates'),
)

FIXTURE_DIRS = (
    os.path.join(PROJECT_PATH, 'fixtures'),
)

# A sample logging configuration.
# This logs all rapidsms messages to the file `rapidsms.log`
# in the project directory.  It also sends an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'formatters': {
        'basic': {
            'format': '%(asctime)s %(name)-20s %(levelname)-8s %(message)s',
        },
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'basic',
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'formatter': 'basic',
            'filename': os.path.join(PROJECT_PATH, 'rapidsms.log'),
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'rapidsms': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'shelterbot': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
        '': {
            'handlers': ['console'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.humanize',
    'django.contrib.sitemaps',
    # Internal apps
    'state_management',
    # External apps
    "django_tables2",
    "selectable",
    'rtwilio',
    # RapidSMS
    "rapidsms",
    "rapidsms.backends.database",
    "rapidsms.contrib.handlers",
    "rapidsms.contrib.httptester",
    "rapidsms.contrib.messagelog",
    "rapidsms.contrib.messaging",
    "rapidsms.contrib.registration",
    "rapidsms.contrib.echo",
    "rapidsms.contrib.default",  # Must be last
)

INSTALLED_BACKENDS = {
    "message_tester": {
        "ENGINE": "rapidsms.backends.database.DatabaseBackend",
    },
}

# Twillio Settings
TWILLIO_ACCOUNT_SID = os.environ.get('TWILLIO_ACCOUNT_SID', None) #TODO: default these for local testing values
TWILLIO_AUTH_TOKEN = os.environ.get('TWILLIO_AUTH_TOKEN', None)
TWILLIO_PHONE_NUMBER = os.environ.get('TWILLIO_PHONE_NUMBER', None)
if TWILLIO_ACCOUNT_SID and TWILLIO_AUTH_TOKEN and TWILLIO_PHONE_NUMBER:
    INSTALLED_BACKENDS["twilio-backend"] = {
        "ENGINE": "rtwilio.outgoing.TwilioBackend",
        'config': {
            'account_sid': TWILLIO_ACCOUNT_SID,  # (required)
            'auth_token': TWILLIO_AUTH_TOKEN,  # (required)
            'number': TWILLIO_PHONE_NUMBER,  # your Twilio phone number (required)
            # optional callback URL
            # 'callback': 'http://<public-django-instance>/backend/twilio/status-callback/',
        }
    }

#Wunderground API settings
WUNDERGROUND_API_KEY = os.environ.get('WUNDERGROUND_API_KEY', None)
WUNDERGROUND_LOCALE = os.environ.get('WUNDERGROUND_LOCALE', None)

LOGIN_REDIRECT_URL = '/'

RAPIDSMS_HANDLERS = (
    'shelterbot.handlers.default.DefaultHandler',
    'rapidsms.contrib.echo.handlers.echo.EchoHandler',
    'rapidsms.contrib.echo.handlers.ping.PingHandler',
    'shelterbot.handlers.help.HelpHandler',
    'shelterbot.handlers.weather.WeatherHandler',
)

ALLOWED_KEYWORDS = {
    "WEATHER": "If you text WEATHER, you will get a report of the expected weather for this evening."
}
