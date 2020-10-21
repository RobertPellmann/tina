import os

ENV_PRODUCTION = 'production'
ENV_DEVELOPMENT = 'development'

def debug(message):
    env = os.environ.get('FLASK_ENV', ENV_PRODUCTION)
    if env == ENV_DEVELOPMENT:
        print(str(message))