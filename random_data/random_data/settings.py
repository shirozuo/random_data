import json
import os
from pathlib import Path

# Define the base directory of the project
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
SECRET_KEY = 'django-insecure-5l-v^a3nw4_lia=j$gr92%%&pq_5jzoa6iiwfwyu-0uq+2q(42'
DEBUG = True
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

# Define installed applications
INSTALLED_APPS = [
    'daphne',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'generator',
    'channels',
    'rest_framework',
    'social_django',
]

# Define middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Define URL configuration
ROOT_URLCONF = 'random_data.urls'

# Define templates settings
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

# Define WSGI and ASGI applications
WSGI_APPLICATION = 'random_data.wsgi.application'
ASGI_APPLICATION = 'random_data.asgi.application'

# Define channel layers configuration
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('127.0.0.1', 6379)],
        },
    },
}

# Define database configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Define authentication backends
AUTHENTICATION_BACKENDS = (
    'social_core.backends.github.GithubOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)

# Load social authentication configuration from a file
with open('config.json') as config_file:
    config = json.load(config_file)

SOCIAL_AUTH_GITHUB_KEY = config['GITHUB_CLIENT_ID']
SOCIAL_AUTH_GITHUB_SECRET = config['GITHUB_CLIENT_SECRET_KEY']

LOGIN_URL = 'login'
LOGOUT_URL = 'logout'
LOGIN_REDIRECT_URL = '/generator'

# Define password validation settings
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

# Internationalization settings
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = 'static/'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Define the log directory
LOG_DIR = os.path.join(BASE_DIR, 'logs')

# Create the log directory if it does not exist
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

# Logging configuration
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        },
        'file_scheduler': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(LOG_DIR, 'scheduler.log'),
            'formatter': 'verbose',
        },
        'file_tasks': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(LOG_DIR, 'tasks.log'),
            'formatter': 'verbose',
        },
        'file_django': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(LOG_DIR, 'django.log'),
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'file_django'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'scheduler': {
            'handlers': ['console', 'file_scheduler'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'tasks': {
            'handlers': ['console', 'file_tasks'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}
