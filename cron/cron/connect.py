from abc import ABC, abstractmethod

from elasticsearch import Elasticsearch

ELASTIC_HOSTS = ["elastic"]


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
        except Exception as err:
            raise Exception(err)
