"""Flask Local Development Environment Configuration."""
import logging

import redis
from config.envs.default import DefaultConfig as Config
from fsd_utils import configclass
from os import environ
from os import path


@configclass
class DevelopmentConfig(Config):
    #  Application Config
    SECRET_KEY = "dev"
    SESSION_COOKIE_NAME = "session_cookie"
    FLASK_ENV = "development"

    # Logging
    FSD_LOG_LEVEL = logging.DEBUG

    # Database
    SQLITE_DB_NAME = "sqlite.db"
    SQLALCHEMY_DATABASE_URI = environ.get(
        "DATABASE_URL"
    ) or "sqlite:///" + path.join(Config.FLASK_ROOT, SQLITE_DB_NAME)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
