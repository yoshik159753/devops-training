import os

PROJECT_NAME = os.getenv("PROJECT_NAME", "app")
LOGGER_LEVEL = os.getenv('LOGGER_LEVEL', 'INFO')

DATABASE_URL = os.getenv('DATABASE_URL', 'driver://user:pass@localhost/dbname')
