from import_export.formats.base_formats import CSV, XLSX, XLS, JSON
import os
import sys
from pathlib import Path
from django.conf import settings
from os.path import join
from decouple import config


# Build paths inside the project like this: BASE_DIR / 'subdir'.
PROJECT_ROOT = os.path.dirname(__file__)

BASE_DIR = Path(__file__).resolve().parent.parent
BASE_BASE_DIR = Path(__file__).resolve().parent.parent.parent
TEMPLATE_DIR = str(BASE_BASE_DIR.joinpath('templates/skeleton/'))

sys.path.insert(0, join(PROJECT_ROOT, "apps"))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-^q52bhy0%%xi(h9rf4ow=7h*^$8y49+g+ig#8_hx7fnba-i^h*'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# SECURE_SSL_REDIRECT=True

# Application definition

INSTALLED_APPS = [
    "daphne",
    "admin_interface",
    "colorfield",
    "admin_notification",

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'django.contrib.humanize',
    'django.contrib.postgres',

    # Local apps
    'apps.core.apps.CoreConfig',
    'apps.api.apps.ApiConfig',





    # Third-party apps
    'channels',
    'rest_framework',
    'rest_framework_simplejwt',
    'corsheaders',

    'utils',
]

MIDDLEWARE = [
    # "django.middleware.cache.UpdateCacheMiddleware",

    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'django.middleware.locale.LocaleMiddleware'


    # "django.middleware.cache.FetchFromCacheMiddleware",
]

ROOT_URLCONF = 'skeleton.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'skeleton.wsgi.application'
ASGI_APPLICATION = 'skeleton.asgi.application'

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [("127.0.0.1", 6379)],
        },
    },
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    },
    'postgres':  {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    },
    'mongodb': {}
}

# DATABASE_ROUTERS=['routers.db_routers.AuthRouter']

INTERNAL_IPS = [
    # ...
    "127.0.0.1",
    # ...
]


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization

LANGUAGE_CODE = 'fa-IR'

TIME_ZONE = 'Asia/Tehran'


# import locale
# locale.setlocale(locale.LC_ALL, "fa_IR.UTF-8")

USE_I18N = True

USE_TZ = True


STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
# STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATICFILES_DIRS = [str(BASE_BASE_DIR.joinpath('static/skeleton/'))]

MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

CKEDITOR_UPLOAD_PATH = "uploads/"

LOGIN_REDIRECT_URL = 'home_view'
LOGOUT_REDIRECT_URL = 'home_view'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'accounts.User'

DEFAULT_FROM_EMAIL = "info@skeleton.com"
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_HOST = 'localhost'
EMAIL_POST = 25
# EMAIL_HOST_USER = config('')
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = True


REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        # 'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',
        # 'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ],

    'DEFAULT_AUTHENTICATION_CLASSES': [
        # 'rest_framework.authentication.TokenAuthentication',
        # 'rest_framework.authentication.SessionAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',

    ],


    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 24
}

SPECTACULAR_SETTINGS = {
    'TITLE': 'skeleton API',
    'DESCRIPTION': 'Your project description',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
    # OTHER SETTINGS
}

CACHES = {
    "default": {
        # "BACKEND": "django.core.cache.backends.redis.RedisCache",
        # "LOCATION": "redis://127.0.0.1:6379",
        # "LOCATION": "redis://username:password@127.0.0.1:6379",

        # "BACKEND": "django.core.cache.backends.filebased.FileBasedCache",
        # "LOCATION": "c:/foo/bar",

        "BACKEND": "django.core.cache.backends.dummy.DummyCache",

        # "BACKEND": "django_redis.cache.RedisCache",
        # "LOCATION": "redis://127.0.0.1:6379/1",
        # "OPTIONS": {
        #     "CLIENT_CLASS": "django_redis.client.DefaultClient",
        # "COMPRESSOR": "django_redis.compressors.zlib.ZlibCompressor",
        # }
    }
}

JALALI_DATE_DEFAULTS = {
    'Strftime': {
        'date': '%y/%m/%d',
        'datetime': '%H:%M:%S _ %y/%m/%d',
    },
    'Static': {
        'js': [
            # loading datepicker
            'admin/js/django_jalali.min.js',
            # OR
            # 'admin/jquery.ui.datepicker.jalali/scripts/jquery.ui.core.js',
            # 'admin/jquery.ui.datepicker.jalali/scripts/calendar.js',
            # 'admin/jquery.ui.datepicker.jalali/scripts/jquery.ui.datepicker-cc.js',
            # 'admin/jquery.ui.datepicker.jalali/scripts/jquery.ui.datepicker-cc-fa.js',
            # 'admin/js/main.js',
        ],
        'css': {
            'all': [
                'admin/jquery.ui.datepicker.jalali/themes/base/jquery-ui.min.css',
            ]
        }
    },
}

# STORAGES = {
#     "default": {
#         "BACKEND": "storages.backends.s3.S3Storage",
#         "OPTIONS": {
#           ...your_options_here
#         },
#     },

# "dropbox": {
#         "BACKEND": "storages.backends.dropbox.DropboxStorage",
#         "OPTIONS": {
#           ...your_options_here
#         },
#     },
# }

IMPORT_EXPORT_FORMATS = [CSV]

GRAPHENE = {
    "SCHEMA": "apps.core.schema.schema"
}

CELERY_TIMEZONE = TIME_ZONE
CELERY_ENABLE_UTC = True
CELERY_TASK_TRACK_STARTED = True
CELERY_TASK_TIME_LIMIT = 30 * 60
# CELERY_BROKER_URL = broker_url = 'amqp://myuser:mypassword@localhost:5672/myvhost'
CELERY_BROKER_URL = 'redis://localhost:6379'
CELERY_RESULT_BACKEND = CELERY_BROKER_URL
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_DEFAULT_QUEUE = 'default'


TAGGIT_CASE_INSENSITIVE = True

X_FRAME_OPTIONS = "SAMEORIGIN"
SILENCED_SYSTEM_CHECKS = ["security.W019"]

NOTIFICATION_MODEL = 'pages.ContactModel'

# SESSION_ENGINE = "django.contrib.sessions.backends.cache"
# SESSION_CACHE_ALIAS = "default"


AZ_IRANIAN_BANK_GATEWAYS = {
    'GATEWAYS': {
        'ZARINPAL': {
            'MERCHANT_CODE': '<YOUR MERCHANT CODE>',
            'SANDBOX': 1,  # 0 disable, 1 active
        },
        'IDPAY': {
            'MERCHANT_CODE': '<YOUR MERCHANT CODE>',
            'METHOD': 'POST',  # GET or POST
            'X_SANDBOX': 1,  # 0 disable, 1 active
        },
    },
    'IS_SAMPLE_FORM_ENABLE': True,  # اختیاری و پیش فرض غیر فعال است
    'DEFAULT': 'ZARINPAL',
    'CURRENCY': 'IRT',  # اختیاری
    'TRACKING_CODE_QUERY_PARAM': 'tc',  # اختیاری
    'TRACKING_CODE_LENGTH': 16,  # اختیاری
    'SETTING_VALUE_READER_CLASS': 'azbankgateways.readers.DefaultReader',  # اختیاری
    'BANK_PRIORITIES': [
        'ZARINPAL',
        'IDPAY',
    ],  # اختیاری
    'IS_SAFE_GET_GATEWAY_PAYMENT': True,  # اختیاری، بهتر است True بزارید.
    'CUSTOM_APP': None,  # اختیاری
}

# ELASTICSEARCH_DSL = {
#     "default": {"hosts": "elasticsearch:9200"},
# }