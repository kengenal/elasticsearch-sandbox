import os
import sqlite3
from abc import ABC, abstractmethod
from pathlib import Path

from elasticsearch import Elasticsearch

ELASTIC_HOSTS = ["elastic"]
SQL_PATH = os.path.join(Path(__file__).resolve().parent.parent.parent / 'database/db.sqlite3')


class ConnectionException(Exception):
    def __init__(self, db):
        super().__init__(f"{db}: Connection error")


class AbstractConnection(ABC):
    @abstractmethod
    def connect(self):
        pass


class ElasticConnect(AbstractConnection):
    def __init__(self):
        """ Connection to elastic serach client """
        self.es = None

    def connect(self):
        try:
            self.es = Elasticsearch(
                hosts=ELASTIC_HOSTS,
                sniff_on_start=True,
                sniff_on_connection_fail=True,
                sniffer_timeout=15
            )
        except Exception:
            raise ConnectionException("elastic")


class SqlConnect(AbstractConnection):
    def __init__(self, path=None):
        self.db_path = SQL_PATH
        if path is not None:
            self.db_path = path
        self.cursor = None
        self.conn = None

    def connect(self):
        try:
            conn = sqlite3.connect(self.db_path)
            self.conn = conn
            self.cursor = conn.cursor()
        except Exception:
            raise ConnectionException("sqlite")
