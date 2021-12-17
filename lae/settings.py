"""
Django settings for lae project.

Generated by 'django-admin startproject' using Django 3.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

import os
from pathlib import Path

import django_heroku
import environ
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

environ.Env.read_env(str(BASE_DIR) + "/.env")

ENV = environ.Env(
    # set casting, default value
    DEBUG=(bool, False),
    DJANGO_SECRET_KEY=(
        str,
        "DQZLA!5wn3uwQHXGH%U4wi2%dmJhwmvh2ko#mMRTa3VK7TibMypi#DZ5x^UEK&oxQ#t4xRun",
    ),
    SITENAME=(str, "*"),
    USE_HEROKU=(bool, False),
    EMAIL_HOST=(str, ""),
    EMAIL_HOST_USER=(str, ""),
    EMAIL_HOST_PASSWORD=(str, ""),
    DEFAULT_FROM_EMAIL=(str, ""),
)

HEROKU_ENV = environ.Env(
    AWS_STORAGE_BUCKET_NAME=(str, ""),
    AWS_ACCESS_KEY_ID=(str, ""),
    AWS_SECRET_ACCESS_KEY=(str, ""),
    HCAPTCHA_TOKEN=(str, ""),
    HCAPTCHA_SECRET_KEY=(str, ""),
    HCAPTCHA_VERIFY_URL=(str, ""),
)

DEBUG = ENV("DEBUG")
SECRET_KEY = ENV("DJANGO_SECRET_KEY")
ALLOWED_HOSTS = [ENV("SITENAME")]
USE_HEROKU = ENV("USE_HEROKU")

EMAIL_HOST = ENV("EMAIL_HOST")
EMAIL_PORT = 587
EMAIL_HOST_USER = ENV("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = ENV("EMAIL_HOST_PASSWORD")
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = ENV("DEFAULT_FROM_EMAIL")

AWS_STORAGE_BUCKET_NAME = HEROKU_ENV("AWS_STORAGE_BUCKET_NAME")
AWS_S3_REGION_NAME = "eu-west-2"
AWS_ACCESS_KEY_ID = HEROKU_ENV("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = HEROKU_ENV("AWS_SECRET_ACCESS_KEY")

HCAPTCHA_TOKEN = HEROKU_ENV("HCAPTCHA_TOKEN")
HCAPTCHA_SECRET_KEY = HEROKU_ENV("HCAPTCHA_SECRET_KEY")
HCAPTCHA_VERIFY_URL = HEROKU_ENV("HCAPTCHA_VERIFY_URL")

if not DEBUG:
    sentry_sdk.init(
        dsn="https://a108d751c93445f79187f5fa0008a988@o1088823.ingest.sentry.io/6103632",
        integrations=[DjangoIntegration()],
        # Set traces_sample_rate to 1.0 to capture 100%
        # of transactions for performance monitoring.
        # We recommend adjusting this value in production.
        traces_sample_rate=1.0,
        # If you wish to associate users to errors (assuming you are using
        # django.contrib.auth) you may enable sending PII data.
        send_default_pii=True,
    )

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "phonenumber_field",
    "crispy_forms",
    "crispy_tailwind",
    "app",
    "accounts",
    "storages",
]

MIDDLEWARE = [
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "csp.middleware.CSPMiddleware",
]

ROOT_URLCONF = "lae.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [str(BASE_DIR.joinpath("templates"))],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "lae.wsgi.application"

STATICFILES_DIRS = [
    BASE_DIR / "static",
]

# Crispy forms theme

CRISPY_ALLOWED_TEMPLATE_PACKS = "tailwind"
CRISPY_TEMPLATE_PACK = "tailwind"

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# Redirect urls after logging in or out

LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
    {"NAME": "lae.password_validators.SymbolValidator"},
    {"NAME": "lae.password_validators.MixedCaseValidator"},
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = "en-gb"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files and media files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Auth user model for authorisation app

AUTH_USER_MODEL = "accounts.User"


# Security settings

PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.ScryptPasswordHasher",
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
]

if not DEBUG:
    CSP_DEFAULT_SRC = "'none'"
    CSP_FONT_SRC = "'self'"
    CSP_STYLE_SRC = ("'self'", "https://*.hcaptcha.com", "https://hcaptcha.com")
    CSP_SCRIPT_SRC = ("'self'", "https://*.hcaptcha.com", "https://hcaptcha.com")
    CSP_IMG_SRC = ("'self'", "https://lovejoy-antique-media.s3.amazonaws.com")
    CSP_CONNECT_SRC = ("'self'", "https://*.hcaptcha.com", "https://hcaptcha.com")
    CSP_FRAME_SRC = ("'self'", "https://*.hcaptcha.com", "https://hcaptcha.com")

    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_HSTS_SECONDS = 31536000
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    CSRF_COOKIE_SECURE = True

# Heroku settings

if USE_HEROKU:
    DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
    STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

    django_heroku.settings(locals())
