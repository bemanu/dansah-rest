"""
Django settings for dansah project.

Generated by 'django-admin startproject' using Django 4.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
import os
from pathlib import Path
import environ

env = environ.Env()
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent

environ.Env.read_env(os.path.join(BASE_DIR, 'prod.env'))

ENVIRONMENT = env('ENVIRONMENT')
print("<<<<<<<<<<<<<USING   " + ENVIRONMENT + ">>>>>>>>>>>>>>>>>>>>>>>")
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG')

print("The value of debug <<<<<<<<====" + DEBUG)
if DEBUG:
    print("THis is in Debug")

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '.vercel.app']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
    'homeactivities',
    'homeevents',
    'homeministriesmaterial',
    'homeslider',
    'profiles',
    'quoteoftheday',
    'role',
    'storages',
    'powerliving',
    'socialmedia',
    'prayerconnect',
    'prayercity',
    'leadershipinstitute',
    'contact',
    'home',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CORS_ALLOW_ALL = False

ROOT_URLCONF = 'dansah.urls'

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

WSGI_APPLICATION = 'dansah.wsgi.application'

# WSGI_APPLICATION = 'vercel_app.wsgi.app'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases
IS_DEV = env('IS_DEV')

if IS_DEV == "True":
    print("this is dev settings <<<<<<<<<<<<<<<<< ==" + IS_DEV)
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }
else:
    print("productions settings database")
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "POSTGRES_DATABASE": env('PGDATABASE'),
            "POSTGRES_USER": env('PGUSER'),
            "POSTGRES_PASSWORD": env('PGPASSWORD'),
            "POSTGRES_HOST": env('PGHOST'),
            "POSTGRES_URL": env('PGURL'),
            "POSTGRES_PRISMA_URL": env('PGPRISMAURL'),
            "POSTGRES_URL_NON_POOLING": env('PGURLNONPOOLING'),

        }
    }
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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static_cdn", 'static')

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static_cdn", "media_root")

USE_S3 = env('USE_S3')
print(USE_S3 + "<<<<<<<<<<<" + USE_S3 + " <<<<<<<<<<<<<<<<<<<<<<<<<,")
if USE_S3:
    print("using S3 settings")
    AWS_ACCESS_KEY_ID = env('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = env('AWS_SECRET_ACCESS_KEY')
    AWS_STORAGE_BUCKET_NAME = env('AWS_STORAGE_BUCKET_NAME')
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
    AWS_DEFAULT_ACL = 'public-read'
    AWS_LOCATION = 'static'
    AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400'}
    AWS_QUERYSTRING_AUTH = False
    AWS_HEADERS = {'Access-Control-Allow-Origin': '*'},
    print("statics files ")
    # s3 static settings
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    STATICFILE_STORAGE = 'storages.backends.s3boto3.S3StaticStorage'

else:
    DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'
    # MEDIA_URL = '/media/'
    # MEDIA_ROOT = BASE_DIR / 'media'
    STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'static')
    STATIC_URL = '/static/'
    # Extra places for collectstatic to find static files.
    # STATIC_ROOT = os.path.join(BASE_DIR, 'static')
    STATICFILES_DIRS = (
        ('admin', os.path.join(BASE_DIR, 'static', 'admin')))

    MEDIA_URL = "/media/"
    # Default primary key field type
    # https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

    MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static_cdn", "media_root")

SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False
SECURE_SSL_REDIRECT = False
SECURE_HSTS_SECONDS = 0

# "ENGINE": env('DATABASE_ENGINE'),
# "NAME": env('PGDATABASE'),
# "USER": env('PGUSER'),
# "PASSWORD": env('PGPASSWORD'),
# "HOST": env('PGHOST'),
# "PORT": env('PGPORT'),
# "ENGINE": "django.db.backends.postgresql",
