# -*- coding: utf-8 -*-
"""
Django settings for referral_project project.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""
from __future__ import absolute_import, unicode_literals

from os.path import join

import environ
from moneyed import USD

from .app_settings import *

ROOT_DIR = environ.Path(__file__) - 3  # (referral_project/config/settings/common.py - 3 = referral_project/)
APPS_DIR = ROOT_DIR.path('referral_project')

env = environ.Env()
env.read_env()

# APP CONFIGURATION
# ------------------------------------------------------------------------------
DJANGO_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
)
THIRD_PARTY_APPS = (
    'crispy_forms',
    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders',
    'djmoney',
    'phonenumber_field',
    'rangefilter',
    'django_cron',
    'constance',
)
LOCAL_APPS = (
    'referral_project.template_filters.apps.TemplateFiltersConfig',

    'referral_project.users.apps.UsersConfig',
    'referral_project.campaigns.apps.CampaignsConfig',
    'referral_project.tasks.apps.TasksConfig',
    'referral_project.wallets.apps.WalletsConfig',
    'referral_project.transactions.apps.TransactionsConfig',
    'referral_project.payment_method.apps.PaymentMethodsConfig',
    'referral_project.admob_credentials.apps.AdmobCredentialConfig'
)
# See: https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

# MIDDLEWARE CONFIGURATION
# ------------------------------------------------------------------------------
MIDDLEWARE_CLASSES = (
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

#CRON CONFIGURATION
CRON_CLASSES = [
    "referral_project.tasks.cron.TaskCronJob",
    "referral_project.users.cron.UserActivationCronJob",
    # ...
]

# MIGRATIONS CONFIGURATION
# ------------------------------------------------------------------------------
MIGRATION_MODULES = {
}

# DEBUG
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = env.bool('DJANGO_DEBUG', False)

# FIXTURE CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-FIXTURE_DIRS
FIXTURE_DIRS = (
    str(APPS_DIR.path('fixtures')),
)

# EMAIL CONFIGURATION
# ------------------------------------------------------------------------------
EMAIL_BACKEND = env('DJANGO_EMAIL_BACKEND', default='django.core.mail.backends.smtp.EmailBackend')

# MANAGER CONFIGURATION
# ------------------------------------------------------------------------------
ADMIN_URL = r'^admin/'
# See: https://docs.djangoproject.com/en/dev/ref/settings/#admins
ADMINS = (
    ("""ITBear""", 'pugach.itbear@gmail.com'),
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#managers
MANAGERS = ADMINS

# DATABASE CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
env.read_env('.env')
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env('POSTGRES_NAME'),
        'USER': env('POSTGRES_USER'),
        'PASSWORD': env('POSTGRES_PASSWORD'),
        'HOST': env('POSTGRES_HOST'),
        'PORT': env('POSTGRES_PORT'),
    }
}

DATABASES['default']['ATOMIC_REQUESTS'] = True

# GENERAL CONFIGURATION
# ------------------------------------------------------------------------------
# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'UTC'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#language-code
LANGUAGE_CODE = 'en-us'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#site-id
SITE_ID = 1

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-i18n
USE_I18N = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-l10n
USE_L10N = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-tz
USE_TZ = True

# TEMPLATE CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#templates
TEMPLATES = [
    {
        # See: https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-TEMPLATES-BACKEND
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-dirs
        'DIRS': [
            str(APPS_DIR.path('templates')),
        ],
        'OPTIONS': {
            # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-debug
            'debug': DEBUG,
            # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-loaders
            # https://docs.djangoproject.com/en/dev/ref/templates/api/#loader-types
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            ],
            # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-context-processors
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
                # Your stuff: custom template context processors go here
            ],
        },
    },
]

# See: http://django-crispy-forms.readthedocs.io/en/latest/install.html#template-packs
CRISPY_TEMPLATE_PACK = 'bootstrap4'

# STATIC FILE CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-root
STATIC_ROOT = str(ROOT_DIR('staticfiles'))

# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-url
STATIC_URL = '/static/'

# See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
STATICFILES_DIRS = (
    str(ROOT_DIR.path('referral_project/static')),
    str(ROOT_DIR.path('referral_project_client/static/dist')),
)

# See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#staticfiles-finders
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

# MEDIA CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-root
MEDIA_ROOT = str(APPS_DIR('media'))

# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-url
MEDIA_URL = '/media/'

_MEDIA_DATE_PATH_FORMAT = join('%Y', '%m', '%d')

_USER_MEDIA_DIR_NAME = 'users'
_USER_IDENTIFICATION_MEDIA_DIR_NAME = 'identification'
USER_IDENTIFICATION_MEDIA_DIR_PATH = join(
    _USER_MEDIA_DIR_NAME,
    _USER_IDENTIFICATION_MEDIA_DIR_NAME,
)

# URL Configuration
# ------------------------------------------------------------------------------
ROOT_URLCONF = 'config.urls'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#wsgi-application
WSGI_APPLICATION = 'config.wsgi.application'

# SLUGLIFIER
AUTOSLUG_SLUGIFY_FUNCTION = 'slugify.slugify'

# Your common stuff: Below this line define 3rd party library settings
# ------------------------------------------------------------------------------
AUTH_USER_MODEL = 'users.User'
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'home'

# Logging
# ---------------------
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s '
                      '%(process)d %(thread)d %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        }
    },
    'loggers': {
        'django.db.backends': {
            'level': 'ERROR',
            'handlers': ['console'],
            'propagate': False,
        },
        'referral_project': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
        },
        'django.security.DisallowedHost': {
            'level': 'ERROR',
            'handlers': ['console'],
            'propagate': False,
        },
    },
}

# CACHING
# ------------------------------------------------------------------------------
CACHES = {
    'default': {
        'BACKEND': 'redis_cache.RedisCache',
        'LOCATION': env('REDIS_HOST', default='redis:6379')
    }
}

# Django REST Framework
# ------------------------------------------------------------------------------
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.MultiPartParser',
    ],
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    ),
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.SearchFilter',
        'rest_framework.filters.OrderingFilter'
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 10,
    'DATETIME_FORMAT': 'iso-8601',
    'EXCEPTION_HANDLER': 'referral_project.utils.rest_framework.exception_handlers.custom_exception_handler',
}

CORS_ORIGIN_ALLOW_ALL = True

# django-money
# ------------------------------------------------------------------------------
DEFAULT_CURRENCY = USD

# User settings
# ------------------------------------------------------------------------------
# TODO: lazy
# NOTE: this is to facilitate testing


REACT_REGISTER_URL = '/#/registration/'

CONSTANCE_CONFIG = {
    'MINIMUM_SENDER_BALANCE': (5, 'Minimum Sender Balance', int),
    'MINIMUM_WITHDRAWAL_AMOUNT': (25, 'Minimum Withdrawal Amount', int),
    'MINIMUM_TRANSFER_AMOUNT': (25, 'Minimum Transfer Amount', int),
    'REFERRAL_BONUS': (5, 'Referral Bonus', int),
    'REFERRAL_WORK_COMMISSIONS': (5, 'Referral Work Commissions', int),
    'ACTIVATION_COST': (30, 'Activation Cost', int),

    'FREE_MIN_DAILY_VIDEO': (5, 'Min Daily Video', int),

    'PAID_MIN_DAILY_VIDEO': (20, 'Min Daily Video', int),
    'PAID_VALIDITY_OF_DAYS': (90, 'Validity Of Days', int),

    'CRON_TASK_CRON_DURATION': (24 * 60 * 60, 'Task Cron Duration', int),
    'CRON_TASK_CRON_START_TIME': ('0:0', 'Task Cron Start Time', str),

    'ADMIN_MINIMUM_MAIN_SENDER_BALANCE': (5, 'Minimum Main Sender Balance', int),
    'ADMIN_MINIMUM_REFER_SENDER_BALANCE': (0, 'Minimum Refer Sender Balance', int),
    'ADMIN_MINIMUM_TRANSFER_SENDER_BALANCE': (5, 'Minimum Transfer Sender Balance', int),
    'ADMIN_MIN_ACTIVE_REFER_USER': (1, 'Minimum Active Refer User', int),
    'ADMIN_FEES_IN_PERCENTAGE': (1, 'Fees In Percentage', int),

    'REGIONAL_ADMIN_MINIMUM_MAIN_SENDER_BALANCE': (5, 'Minimum Main Sender Balance', int),
    'REGIONAL_ADMIN_MINIMUM_REFER_SENDER_BALANCE': (5, 'Minimum Refer Sender Balance', int),
    'REGIONAL_ADMIN_MIN_ACTIVE_REFER_USER': (1, 'Minimum Active Refer User', int),
    'REGIONAL_ADMIN_FEES_IN_PERCENTAGE': (1, 'Fees In Percentage', int),
}

CONSTANCE_CONFIG_FIELDSETS = {
    'Any': ('MINIMUM_SENDER_BALANCE', 'MINIMUM_WITHDRAWAL_AMOUNT', 'MINIMUM_TRANSFER_AMOUNT', 'REFERRAL_BONUS', 'REFERRAL_WORK_COMMISSIONS', 'ACTIVATION_COST'),
    'Free': ('FREE_MIN_DAILY_VIDEO',),
    'Paid': ('PAID_MIN_DAILY_VIDEO', 'PAID_VALIDITY_OF_DAYS'),
    'Cron': ('CRON_TASK_CRON_DURATION', 'CRON_TASK_CRON_START_TIME'),
    'Admin Wallet': ('ADMIN_MINIMUM_MAIN_SENDER_BALANCE', 'ADMIN_MINIMUM_REFER_SENDER_BALANCE', 'ADMIN_MINIMUM_TRANSFER_SENDER_BALANCE'),
    'Admin Withdraw Request': ('ADMIN_MIN_ACTIVE_REFER_USER', 'ADMIN_FEES_IN_PERCENTAGE'),
    'Regional Admin Wallet': ('REGIONAL_ADMIN_MINIMUM_MAIN_SENDER_BALANCE', 'REGIONAL_ADMIN_MINIMUM_REFER_SENDER_BALANCE'),
    'Regional Admin Withdraw Request': ('REGIONAL_ADMIN_MIN_ACTIVE_REFER_USER', 'REGIONAL_ADMIN_FEES_IN_PERCENTAGE'),
}

CONSTANCE_REDIS_CONNECTION = {
    'host': 'redis',
    'port': 6379,
    'db': 0,
}
