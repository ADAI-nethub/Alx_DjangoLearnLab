# social_media_api/settings/production.py
from .base import *

# Security settings - like adding locks and alarms
DEBUG = False  # Don't show blueprints to visitors!
ALLOWED_HOSTS = ['your-domain.com', 'www.your-domain.com', 'localhost']  # Who can visit

# Database - stronger foundation
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT', '5432'),
    }
}

# Security headers - like reinforced doors and windows
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'  # Don't let others embed your site
SECURE_SSL_REDIRECT = True  # Always use HTTPS
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# Static files - using a professional storage service
AWS_S3_REGION_NAME = 'your-region'
AWS_STORAGE_BUCKET_NAME = 'your-bucket-name'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3StaticStorage'