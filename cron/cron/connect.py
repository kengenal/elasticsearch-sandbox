from abc import ABC, abstractmethod

from elasticsearch import Elasticsearch

ELASTIC_HOSTS = ["localhost", "elastic"]


class AbstractConnection(ABC):
    @abstractmethod
    def connect(self):
        pass


class ElasticConnect(AbstractConnection):
    def __init__(self):
        """ Connection to elastic serach client """
        self.es = None

    def connect(self):
        self.es = Elasticsearch(
            ELASTIC_HOSTS,
        )
