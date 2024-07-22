from pathlib import Path
import environ


env = environ.Env(
    DEBUG=(bool, True)
)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

env.read_env('.env')

# SECURITY_WARNING: keep the secret key used in production secret!
SECRET_KEY = env("SECRET_KEY")
# SECURITY_WARNING: don't run with debug turned on in production!
DEBUG = env("DEBUG")


ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")


# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # third-party
    'rest_framework',
    'django_filters',

    # authentication
    'rest_framework.authtoken',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'dj_rest_auth',
    'dj_rest_auth.registration',

    # documentation swagger
    'drf_yasg',

    # local apps
    'apps.common',
    'apps.metadata',
    'apps.novels',
    'apps.chapters',
    'apps.users',
    'apps.teams',
    'apps.authentication',
    'apps.libraries',
    'apps.bookmarks',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'allauth.account.middleware.AccountMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'apps.common.middlewares.RequestLoggingMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'config.wsgi.application'

DATABASES = {
    'default': env.db()
}

AUTH_USER_MODEL = 'users.User'

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
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

SITE_ID = 1

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend'
    ],
    'EXCEPTION_HANDLER': 'apps.common.exceptions.api_exception_handler'
}

# dj-rest-auth settings
REST_AUTH = {
    'REGISTER_SERIALIZER': 'apps.authentication.serializers.RegisterSerializer',
    'LOGIN_SERIALIZER': 'apps.authentication.serializers.LoginSerializer'
}

# Email setup
EMAIL_CONFIRM_REDIRECT_BASE_URL = 'http://localhost:8000/email/confirm/'
PASSWORD_RESET_CONFIRM_REDIRECT_BASE_URL = \
    'http://localhost:8000/password-reset/confirm/'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_HOST = env('EMAIL_HOST')
EMAIL_USE_TLS = env('EMAIL_USE_TLS')
EMAIL_PORT = env('EMAIL_PORT')
EMAIL_HOST_USER = env('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = env('DEFAULT_FROM_EMAIL')

# allauth
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = "mandatory"


LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,

    "formatters": {
        "simple": {
            "format": "[{levelname}:{asctime}]: {message}",
            "style": "{"
        },
    },

    "handlers": {
        "debug_file": {
            "level": "DEBUG",
            "formatter": "simple",
            "class": "logging.handlers.RotatingFileHandler",
            "maxBytes": 1024*100,
            "backupCount": 5,
            "filename": "./logs/debug.log"
        },
        "request_file": {
            "level": "DEBUG",
            "formatter": "simple",
            "class": "logging.handlers.RotatingFileHandler",
            "maxBytes": 1024*100,
            "backupCount": 5,
            "filename": "./logs/requests.log"
        },
        "console": {
            "level": "INFO",
            "formatter": "simple",
            "class": "logging.StreamHandler",
        }
    },

    "loggers": {
        "drf_requests": {
            "level": "DEBUG",
            "handlers": ["request_file"],
        },
        "apps": {
            "level": "INFO",
            "handlers": ["console"]
        },
        "": {
            "level": "DEBUG",
            "handlers": ["debug_file"],
        },
    }
}

DEFAULT_LIBRARY_NAMES = [
    'Читаю',
    'Буду читать',
    'Прочитано',
    'Любимые'
]
