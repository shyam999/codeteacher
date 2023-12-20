"""
Django settings for educa project.
"""
import os
from pathlib import Path
from django.urls import reverse_lazy

BASE_DIR = Path(__file__).resolve(strict=True).parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'cee03l^mxz0-*^mg4v7_3vf49y&j+y)babltls=(-!=29=$j4^'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'ckeditor',
    'memcache_status',

    'courses.apps.CoursesConfig',
    'students.apps.StudentsConfig',
    'blog.apps.BlogConfig',
]

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'educa.urls'

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

WSGI_APPLICATION = 'educa.wsgi.application'


# Database Settings
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTHENTICATION_BACKENDS = [ 'django.contrib.auth.backends.ModelBackend',
                           'allauth.account.auth_backends.AuthenticationBackend']

# Password validation
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

EMAIL_BACKEND='django.core.mail.backends.console.EmailBackend'

# Custom allauth settings to Use email as the primary identifier
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True

ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_LOGIN_ATTEMPTS_LIMIT = 5

ACCOUNT_LOGOUT_REDIRECT_URL ='/accounts/login/'
LOGIN_REDIRECT_URL = '/accounts/email/'

# Internationalization
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


CKEDITOR_UPLOAD_PATH = "uploads/"

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Advanced',
        'width': 758,
        'height': 300,
        'extraPlugins': 'codesnippet',
    },
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}

# Static files (CSS, JavaScript, Images)
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')


STRIPE_PUBLISHABLE_KEY = 'pk_test_iTsOKmj96ficjj1LRn3RBIPQ00EkPeVDZg'
STRIPE_SECRET_KEY = 'sk_test_YnIaVaIZ3rfWmzsKVbbIofqV00Hxfe7nr1'
