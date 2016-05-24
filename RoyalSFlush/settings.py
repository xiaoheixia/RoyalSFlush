# coding=utf-8
import os

# 基础信息设置
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
APP_CODE = 'RoyalSFlush'
SECRET_KEY = '4b-3kdjw*)9+om+38pu%98!a@rvu$v7(k7#u7(txk!#9(n^6^#'
ALLOWED_HOSTS = ['*']

# 设置环境变量:
# 主要分为   1、DEV --开发环境   
#       2、STG --测试环境  
#       3、PRD --生产环境
WSGI_ENV = os.environ.get("DJANGO_CONF_MODULE", "DEV")

RUN_MODE = 'DEV'
if WSGI_ENV.endswith("PRD"):
    RUN_MODE = "PRD"
    DEBUG = False
elif WSGI_ENV.endswith("STG"):
    RUN_MODE = "STG"
    DEBUG = False
else:
    RUN_MODE = "DEV"
    DEBUG = True

#DEBUG = False
TEMPLATE_DEBUG = DEBUG

# 项目包含app设置
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'dashboard',
)

# WSGI等相关配置设定
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'RoyalSFlush.urls'
WSGI_APPLICATION = 'RoyalSFlush.wsgi.application'

# 模板方案设置
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)
TEMPLATE_DIRS = (
   os.path.join(BASE_DIR, 'templates'),
   # os.path.join(BASE_DIR,'templates').replace('\\','/'),
)

# 数据库配置设置，可以选择mysql,默认选择sqlite3
#DATABASES = {
#    'default': {
#        # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
#        'ENGINE': 'django.db.backends.mysql',
#        'NAME': 'RoyalSFlush',
#        'USER': 'root',
#        'PASSWORD': 'root',
#        'HOST': '127.0.0.1',
#        'PORT': '3306',
#    }
#}

DATABASES = {
    'default': {
        # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR,'RoyalSFlushDB.sqlite3'),
    }
}

# 语言和时区设置
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# 静态资源设置
STATIC_ROOT = os.path.join(BASE_DIR, 'collectedstatic').replace('\\', '/')
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static').replace('\\', '/'),
)
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

# 定义日志打印目录，以及设置日志级别
LOGGING_DIR = os.path.join(BASE_DIR, 'logs', APP_CODE)
LOG_CLASS = 'logging.handlers.RotatingFileHandler'
LOG_LEVEL = 'DEBUG'

# 自动创建LOG目录 
if not os.path.exists(LOGGING_DIR):
    try:
        os.makedirs(LOGGING_DIR)
    except:
        pass
    
# 创建日志打印规则
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s [%(asctime)s] %(pathname)s %(lineno)d %(funcName)s %(process)d %(thread)d \n \t %(message)s \n',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
        'simple': {
            'format': '%(levelname)s %(message)s \n'
        },
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'django.utils.log.NullHandler',
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'root': {
            'class': LOG_CLASS,
            'formatter': 'verbose',
            'filename': os.path.join(LOGGING_DIR, '%s.log' % APP_CODE),
            'maxBytes': 1024 * 1024 * 10,
            'backupCount': 5
        },
        'sqlitedb':{
            'class':LOG_CLASS,
            'formatter':'verbose',
            'filename':os.path.join(LOGGING_DIR,'sqlitedb.log'),
            'maxBytes':1024*1024*4,
            'backupCount':5
        },
    },
    'loggers': {
        'django': {
            'handlers': ['null'],
            'level': 'INFO',
            'propagate': True,
        },
        'django.request': {
            'handlers': ['console'],
            'level': 'ERROR',
            'propagate': True,
        },
        'root': {
            'handlers': ['root'],
            'level': LOG_LEVEL,
            'propagate': True,
        },
        'django.db.backends': {
            'handlers': ['sqlitedb'],
            'level': 'DEBUG',
            'propagate': True,
        },
    }
}