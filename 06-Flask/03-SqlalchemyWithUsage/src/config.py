import os
from dotenv import load_dotenv
load_dotenv('../.env')


class Config:
    DEBUG = False
    DEVELOPMENT = False


class ProductionConfig(Config):
    ENV = "production"
    SECRET_KEY = os.getenv("SECRET_KEY")
    HELLO_WORLD = os.getenv("HELLO_WORLD")

    # @property
    # def POSTGRES_URI(self):
    #     return f"mysql://user@{self.SECRET_KEY}/foo"


class DevelopmentConfig(Config):
    ENV = "development"
    DEBUG = True
    DEVELOPMENT = True

    SECRET_KEY = os.getenv("SECRET_KEY")
    HELLO_WORLD = os.getenv("HELLO_WORLD")

    # Postgres
    POSTGRES_HOST = 'localhost'
    POSTGRES_PORT = 5432
    POSTGRES_USER = 'root'
    POSTGRES_PASSWORD = '123123aa'
    POSTGRES_DB = 'todo'
    POSTGRES_URI = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"