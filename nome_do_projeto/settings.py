from pathlib import Path
import os
import dj_database_url

# BASE_DIR é a pasta raiz do seu projeto (a pasta que contém manage.py)
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-s@p+9ruhs5l%gb_6$*ns14*pox0y0xx$u@c*bd5cdl*djx)9zx'
SECRET_KEY = os.getenv('SECRET_KEY', 'django-insecure-default-key')

DEBUG = True

ALLOWED_HOSTS = [host.strip() for host in os.getenv("ALLOWED_HOSTS", "").split(",") if host.strip()]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
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

ROOT_URLCONF = 'nome_do_projeto.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'projeto' / 'templates'],  
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'nome_do_projeto.wsgi.application'

DATABASES = {
    'default': dj_database_url.config()
}

AUTH_PASSWORD_VALIDATORS = [
    # validações de senha padrão
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Configuração dos arquivos estáticos
STATIC_URL = '/static/'

# Caminhos adicionais onde o Django vai procurar arquivos estáticos
STATICFILES_DIRS = [BASE_DIR / 'projeto' / 'static']

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_REDIRECT_URL = 'pag_inicial'

MEDIA_URL = '/media/'
#MEDIA_ROOT = BASE_DIR / 'media'

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

INSTALLED_APPS += ['storages']
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
AWS_ACCESS_KEY_ID = 'SUA_CHAVE'
AWS_SECRET_ACCESS_KEY = 'SUA_CHAVE_SECRETA'
AWS_STORAGE_BUCKET_NAME = 'NOME_DO_BUCKET'
AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/'
AWS_DEFAULT_ACL = 'public-read'

