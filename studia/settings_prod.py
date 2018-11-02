DEBUG = False

ALLOWED_HOSTS = ["*"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'db1',
        'USER': 'django_studio',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '',
    }
}