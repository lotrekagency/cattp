from django.conf import settings
settings.configure(
    DATABASES={'default': {'ENGINE': 'django.db.backends.sqlite3'}},
    TEMPLATES=[{
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
    }],
    AES_ENCRIPTION_KEY='abcdefgh01234567',
    INSTALLED_APPS=[
        'django.contrib.contenttypes',
        'django.contrib.auth',
    ],
)
