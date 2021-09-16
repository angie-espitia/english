import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '@)pys&^6vh&-pitc#u_!2r4h!g6wr5p#q9%pj#4w%na*r6--i3'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'project',
    'project.templatetags',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    # 'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'english.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 'english.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases
#import urlparse
#db_url = urlparse.urlparse(os.environ.get('OPENSHIFT_MYSQL_DB_URL'))

DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),

        'ENGINE': 'django.db.backends.postgresql_psycopg2',
         'NAME': 'dchhsib5k4lfjj',
         'USER': 'iltfvrrxeeruhq',
         'PASSWORD': '21a33502fa52a32396a2e3580cd9dcab8a90243da53a5b4aa385effcee72b5e3',
         'HOST': 'ec2-54-175-77-250.compute-1.amazonaws.com',
         'PORT': '5432',

        # 'ENGINE': 'django.db.backends.postgresql_psycopg2',
        #  'NAME': 'english',
        #  'USER': 'postgres',
        #  'PASSWORD': '1234567',
        #  'HOST': '127.0.0.1',
        #  'PORT': '5432',

        # 'ENGINE': 'django.db.backends.mysql',
        # 'NAME': 'bd_english',
        # 'USER': 'root',
        # 'PASSWORD': '1234567',
        # 'HOST': 'localhost',
        # 'PORT': '3306',
        # 'STORAGE_ENGINE': 'INNODB'
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'es'
TIME_ZONE = 'America/Bogota'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
#URL para acceder a los archivos estaticos
STATIC_URL = '/static/'
STATIC_ROOT = 'staticfiles'

#Directorio donde se almacenaran archivos css
STATICFILES_DIRS = [ BASE_DIR + '/static' ]
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

STATIC_ROLS = {'Estudiantes': 1, 'Profesores': 2}

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_POST = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'ingles.easy1@gmail.com'
EMAIL_HOST_PASSWORD = 'englisheasyplease'

# Cargue para heroku
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
