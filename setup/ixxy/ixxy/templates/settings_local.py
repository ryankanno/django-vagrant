import os

DEBUG = True
TEMPLATE_DEBUG = True
LOCAL_DEV = True
OFFLINE = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': '',
        'PORT': '',
        'NAME': '{{ project }}',
        'USER': 'root',
        'TEST_NAME': None,
    }
}

MEDIA_URL = '/media/'
STATIC_URL = '/static/'
ADMIN_MEDIA_PREFIX = STATIC_URL+'admin/'
FEINCMS_ADMIN_MEDIA = STATIC_URL+'js/tree_editor/'

# CMS App needs RELATIVE_MEDIA_URL set to MEDIA_URL without a server name. This code probably should be moved to the CMS app
if MEDIA_URL.startswith('http:'):
    RELATIVE_MEDIA_URL = ('/'+'/'.join(MEDIA_URL.split('/')[3:]))[:-1]
else:
    RELATIVE_MEDIA_URL = MEDIA_URL

PREPEND_WWW = False

MIDDLEWARE_CLASSES_LOCAL = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

INSTALLED_APPS_LOCAL = (
    'debug_toolbar',
)

SEND_BROKEN_LINK_EMAILS=False

############## CMS settings #################

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': os.path.join(os.path.split(os.path.normpath(os.path.dirname(__file__)))[0], 'django_cache'),
    'JOHNNY_CACHE': True,
    }
}

HIDE_MEMCACHED_WARNING = True
SEND_EMAILS = True
EMAIL_TEST_RECIPIENTS = ['your@email.address',]

############## Django Compressor settings #################

COMPRESS = False

############## Filebrowser settings #################

FILEBROWSER_URL_WWW = MEDIA_URL+'/documents/'
FILEBROWSER_URL_FILEBROWSER_MEDIA = STATIC_URL+"filebrowser/"

############## Django-backup settings #################

BACKUP_SQLDUMP_PATH = 'mysqldump'
BACKUP_FTP_DIRECTORY = 'test'

############## Contact settings ##############

CONTACT_LINK_SUBSCRIBERS_TO_MAILCHIMP = False

############## Maintenance settings ##############

MAINTENANCE_MODE = False

################ Sorl Thumbnail settings ###############

THUMBNAIL_DUMMY = True # Test Site Setting
THUMBNAIL_DEBUG = False

################ Jimmy Page settings ###############

JIMMY_PAGE_DEBUG_CACHE = False
JIMMY_PAGE_DISABLED = True
