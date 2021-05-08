import logging
import os

class Config:

    DEBUG = False
    LOCAL = False
    SECRET_KEY = os.urandom(128)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TEST_WORD = "THIS IS DEV CONFIG?"
    SQLALCHEMY_DATABASE_URI = None
    SQLALCHEMY_ENGINE_OPTIONS = {
        "pool_pre_ping": True,
        "pool_reset_on_return": "rollback",
    }

    def __init__(self) -> None:
        self.SQLALCHEMY_DATABASE_URI = self.get_database_uri(local = self.LOCAL)

    def get_database_uri(self, local = False):
        if not local:
            DB_HOST = os.environ.get("POSTGRES_HOST")
            DB_USER = os.environ.get("POSTGRES_USER")
            DB_PASSWORD = os.environ.get("POSTGRES_PASSWORD")
            DB_NAME = os.environ.get("POSTGRES_DB")
            prefix = "postgresql+psycopg2://"
            body = f"{DB_USER}:{DB_PASSWORD}@{DB_HOST}:5432/{DB_NAME}"
            uri = f"{prefix}{body}"
        else:
            uri = "postgresql+psycopg2://jayse_test:test@localhost:5432/test_db"
        logging.error("local:", local)
        logging.error("uri:", uri)
        return uri

class DevConfig(Config):
    """ DevConfig """

class TestConfig(Config):

    LOCAL = True
    TEST_WORD = "THIS IS TEST CONFIG?"

    def __init__(self) -> None:
        super().__init__()
