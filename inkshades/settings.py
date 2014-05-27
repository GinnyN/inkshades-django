"""
Django settings for inkshades project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '4!hut)u^p6c2&3j+o(j=a7+fjbwpq20qthfw%!ctyr@^d&txv^'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'front',
    'back',
    'south',
    'django_summernote',
    'captcha'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'inkshades.urls'

WSGI_APPLICATION = 'inkshades.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'es-cl'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

import os
ABSOLUTE_PATH           = os.path.dirname(__file__)
MEDIA_ROOT              = os.path.join(ABSOLUTE_PATH, '../media')
MEDIA_URL               = '/media/'
STATIC_ROOT             = os.path.join(ABSOLUTE_PATH, '../static')
STATIC_URL              = '/static/'

TEMPLATE_DIRS = [os.path.join(ABSOLUTE_PATH, '../templates')]

STATICFILES_DIRS = (
  os.path.join(ABSOLUTE_PATH, '../static-development/'),
)

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'satelliteg@gmail.com'
EMAIL_HOST_PASSWORD = 'Imaginate!56'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

LOGIN_URL = "/back/"
LOGOUT_URL = "/back/"