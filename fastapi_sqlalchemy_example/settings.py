from starlette.config import Config
from starlette.datastructures import URL, Secret

config = Config('.env')

DEBUG = config('DEBUG', cast=bool, default=False)
DATABASE_URL = config('DATABASE_URL', cast=URL)
SECRET = config('SECRET', cast=Secret)

EMAIL_SENDER = config('EMAIL_SENDER', default='sender@example.org')
EMAIL_SERVER = config('EMAIL_SERVER', default='localhost')
EMAIL_PORT = config('EMAIL_PORT', cast=int, default=0)
EMAIL_LOGIN = config('EMAIL_LOGIN', default=None)
EMAIL_PASSWORD = config('EMAIL_PASSWORD', default=None)
EMAIL_USE_TLS = config('EMAIL_USE_TLS', cast=bool, default=False)
EMAIL_USE_SSL = config('EMAIL_USE_SSL', cast=bool, default=False)
