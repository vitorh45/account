import json
from os import getenv, path

import logging


class BaseConfig(object):
    DEBUG = True
    TESTING = True
    DEPLOY_ENV = getenv("DEPLOY_ENV", default="Development")
    LOGS_LEVEL = logging.INFO

    JWT_CACHE_EXPIRATION_SECONDS = getenv("JWT_CACHE_EXPIRATION_SECONDS", default=3600)
    SQLALCHEMY_DATABASE_URI = getenv("SQLALCHEMY_DATABASE_URI", default="")
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_MODEL_DIR = path.join(path.dirname(path.dirname(__file__)), 'api', 'infrastructure', 'database')
    SQLALCHEMY_MIGRATE_REPO = path.join(path.dirname(path.dirname(__file__)), 'migrations')
    
    LOGIN_USERNAME = getenv("LOGIN_USERNAME")
    LOGIN_PASSWORD = getenv("LOGIN_PASSWORD")
    JWT_SECRET_KEY = getenv("JWT_SECRET_KEY")



class DevelopmentConfig(BaseConfig):
    DEBUG = True


class TestingConfig(BaseConfig):
    DEBUG = True
    TESTING = True

    JWT_CACHE_EXPIRATION_SECONDS = 3600
    SQLALCHEMY_DATABASE_URI = getenv("SQLALCHEMY_DATABASE_URI_TEST", default="")


class StagingConfig(BaseConfig):
    pass


class ProductionConfig(BaseConfig):
    LOGS_LEVEL = getenv("LOGS_LEVEL", default=logging.INFO)
