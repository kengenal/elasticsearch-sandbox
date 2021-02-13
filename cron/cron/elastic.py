from elasticsearch import Elasticsearch

from .mapping.pypi import pypi_package


class Index:
    def __init__(self, es: Elasticsearch, data):
        """
        Elasticserach pypi_index
        :param es:
        :param data:
        """
        self.es = es
        self.data = data
        self.index_name = "search"

    def clear_index(self):
        """ remove all documents and put mapping, if index not exists create it """
        self.es.delete_by_query(index=self.index_name, body={"query": {"match_all": {}}})
        self.es.indices.put_mapping(index=self.index_name, body=pypi_package, ignore=[400])
        if not self.es.indices.exists(index=self.index_name):
            self.es.indices.create(index=self.index_name)

    def create(self):
        """ Create documents form data """
        if self.data:
            for inx, i in enumerate(self.data):
                self.es.index(index=self.index_name, body=i, id=inx)
