import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


SECRET_KEY = 'hf&y$+n4mis@*@vxu6!np(ert#omh4aih%wlz-q&ys%$zu!e)o'

DEBUG = True

ALLOWED_HOSTS = []



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}



STATIC_DIR = os.path.join(BASE_DIR, 'static')
STATIC_DIRS = [STATIC_DIR]
