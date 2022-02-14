from .base import *

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE'   : 'django.db.backends.mysql',
        'NAME'     : 'STOCK',
        'USER'     : 'root',
        'HOST'     : '192.168.10.151',
        'PASSWORD' : 'rootroot',
        'PORT'     : '33061',
        'CHARSET'  : 'utf8mb4',
        'COLLATION': 'utf8mb4_unicode_ci',

        'OPTIONS'  : {
            'init_command'   : 'SET default_storage_engine=INNODB',
            'isolation_level': 'repeatable read',
            # 'read_default_file': '/path/to/my.cnf',
        },

        'TEST'     : {
            'CHARSET'  : 'utf8mb4',
            'COLLATION': 'utf8mb4_unicode_ci',
        }
    },
}
