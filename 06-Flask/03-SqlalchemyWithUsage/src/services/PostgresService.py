from flask import Config
from src.core.metaclass.Singleton import Singleton
import psycopg2


class PostgresService(metaclass=Singleton):
    __env: Config = None

    def initialize(self, env):
        self.__host = 'localhost'
        self.__port = 5432
        self.__user = 'root'
        self.__password = '123123aa'
        self.__database = 'todo'
        psycopg2.connect(self.__host, self.__port,
                         self.__user,
                         self.__password,
                         self.__database
                         )
        return PostgresService()

    def get_all(self):
        return self.__env.copy()

    def get_one(self, key):
        return self.__env.get(key)
