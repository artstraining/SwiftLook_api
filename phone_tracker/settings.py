from datetime import timedelta
from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-48kh6q*a6*mo2b#6j3)*-8_x)t54q2yd2zs78nchnfz4dq^jyi'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = ['swiftlook-api-jmvy.onrender.com', '127.0.0.1', 'localhost','localhost:5173', 'arts-new-project.vercel.app']

# Application definition

SITE_ID = 1

# INSTALLED_APPS = [
#     'django.contrib.admin',
#     'django.contrib.auth',
#     'django.contrib.contenttypes',
#     'django.contrib.sessions',
#     'django.contrib.messages',
#     'django.contrib.staticfiles',
#     'users',
#     'devices',
#     'admin_dashboard',

#     'django.contrib.sites',
#     'allauth',
#     'allauth.account',
#     'allauth.socialaccount',
#     'allauth.socialaccount.providers.google',

# ]


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'users',
    'devices',
    'admin_dashboard',
    'django.contrib.sites', 
    'allauth', 
    'allauth.account', 
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',  # Add Google provider
    'rest_framework.authtoken',

    # 'dj_rest_auth',  # Rest Auth
    # 'dj_rest_auth.registration',
    ]


REST_USE_JWT = True  # If using JWT with dj-rest-auth
ACCOUNT_EMAIL_VERIFICATION = 'none'  # Optional, based on your requirements
ACCOUNT_EMAIL_REQUIRED = True



SOCIALACCOUNT_ADAPTER = 'allauth.socialaccount.adapter.DefaultSocialAccountAdapter'




MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'allauth.account.middleware.AccountMiddleware',  # Add this line
]


ROOT_URLCONF = 'phone_tracker.urls'

AUTH_USER_MODEL = 'users.CustomUser'


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],

    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 15,  # Set default page size to 15 items
}


SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=360),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=10),
    "SIGNING_KEY": SECRET_KEY,
    "AUTH_HEADER_TYPES": ("Bearer",),  # This requires 'Bearer' prefix in the header
}




TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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


WSGI_APPLICATION = 'phone_tracker.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'swiftlookdb',
        'USER': 'swiftlookdb_user',
        'PASSWORD': 'i65E2SJtvbTziJRrLJ5x5LG71GApT9Hv',
        'HOST': 'dpg-cs9ncbo8fa8c73cd88t0-a.oregon-postgres.render.com',
        'PORT': '5432',  # Default PostgreSQL port
        'OPTIONS': {
            'sslmode': 'require',  # This ensures a secure connection
        },
    }
}

# Email configuration
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.gmail.com'  # Your SMTP server address
# EMAIL_PORT = 587  # Your SMTP server port (587 is the default for SMTP with TLS)
# EMAIL_USE_TLS = True  # Whether to use TLS (True by default)
# EMAIL_HOST_USER = 'artstraining.co.uk@gmail.com'
# EMAIL_HOST_PASSWORD = 'teoa fgdi draf suok'  #teoa fgdi draf suok
# DEFAULT_FROM_EMAIL = 'artstraining.co.uk@gmail.com'  # The default email address to use for sending emails
# EMAIL_DEBUG = True

# Email configuration


EMAIL_HOST = 'smtp.hostinger.com'
EMAIL_USE_TLS = False
EMAIL_USE_SSL = True  # If your SMTP provider uses SSL
EMAIL_PORT = 465  # SSL port
EMAIL_HOST_USER = 'support@sterlingspecialisthospitals.com'
EMAIL_HOST_PASSWORD = '123@Qwertyqwerty123'
DEFAULT_FROM_EMAIL = 'support@sterlingspecialisthospitals.com'
EMAIL_DEBUG = True


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

# Configure CORS
CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",
    "https://swiftlookv1.vercel.app/" # Add your frontend's origin here
    # Add any other origins you want to allow
]

# Optional: Allow all origins (for development only)
CORS_ALLOW_ALL_ORIGINS = True


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True




STATIC_URL = 'static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend"
)


LOGIN_REDIRECT_URL = "https://artstraining.co.uk/dashboard"
LOGOUT_REDIRECT_URL = "/"
