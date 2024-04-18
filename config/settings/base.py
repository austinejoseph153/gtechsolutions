from pathlib import Path
import os
import environ
import dj_database_url


ROOT_DIR = (environ.Path(__file__) - 3) # (techapps/config/settings/base.py - 3 = shoreusa/)
APPS_DIR = ROOT_DIR.path("techapps")

env = environ.Env()

READ_DOT_ENV_FILE = env.bool("DJANGO_READ_DOT_ENV_FILE", default=True)
if READ_DOT_ENV_FILE:
    # OS environment variables take precedence over variables from .env
    env.read_env(str(ROOT_DIR.path(".env")))

# environmental variable setup
env = environ.Env()
environ.Env.read_env('.env')


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/
DEBUG = env.bool("DEBUG", False)


# Application definition
DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles'
]
THIRD_PARTY_APPS = [
    'drf_yasg',
    'ckeditor',
    'ckeditor_uploader',
]
LOCAL_APPS = [
    'techapps.techorders.apps.TechordersConfig',
    'techapps.techblog.apps.TechblogConfig',
    'techapps.techpages.apps.TechpagesConfig'
]
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [str(APPS_DIR.path("templates"))],
        'OPTIONS': {
            "loaders": [
                "django.template.loaders.filesystem.Loader",
                "django.template.loaders.app_directories.Loader",
            ],
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': env('DATABASE_NAME'),
#         'USER': env('DATABASE_USER'),
#         'PASSWORD': env('DATABASE_PASSWORD'),
#         'HOST': env('DATABASE_HOST', default='localhost'),
#         'PORT': 3306
#     }
# }
# else:
DATABASES = {
    'default': dj_database_url.config(
        default=env('DATABASE_URL'),
        conn_max_age=600
    )
}

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/



# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

#STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'



# static files configurations
STATIC_URL = '/static/'
STATIC_ROOT = str(ROOT_DIR("staticfiles"))
STATICFILES_DIRS = [str(APPS_DIR.path("static"))]
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

# media files configurations
MEDIA_URL = '/media/'
MEDIA_ROOT = str(APPS_DIR("media"))
# MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{AWS_LOCATION}/media/'

 

# email configurations
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587.
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = 'austinejoseph60@gmail.com'
DEFAULT_FROM_EMAIL = ""

# aws email configurations for production environment
# EMAIL_BACKEND = 'django_ses.SESBackend'
# AWS_ACCESS_KEY_ID = env('AWS_ACCESS_KEY_ID')
# AWS_SECRET_ACCESS_KEY = env('AWS_SECRET_ACCESS_KEY') 
# AWS_SES_REGION_NAME = env('AWS_S3_REGION_NAME')
# AWS_SES_REGION_ENDPOINT ='REGION-ENDPOINT' #(ex: email.us-east-2.amazonaws.com)
# AWS_STORAGE_BUCKET_NAME = env('AWS_STORAGE_BUCKET_NAME')
# AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
# AWS_LOCATION = 'file'
# AWS_S3_FILE_OVERWRITE=False


ADMINS = [("austine","austinejoseph60@gmail.com"),("gabriel","aulegabriel381@gmail.com")]
MANAGERS = ADMINS

# DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

CKEDITOR_UPLOAD_PATH = "ckeditor_uploads/"
CKEDITOR_ALLOW_NONIMAGE_FILES = False

