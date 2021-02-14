from .connect import ElasticConnect, ConnectionException, SqlConnect
from .elastic import Index
from .sql import UpdateTable


class DataSync:
    def __init__(self, data):
        self.data = data

    def sync_all(self):
        try:
            self.sync_sql()
            self.sync_elastic()
        except Exception as err:
            print(err)
            raise ConnectionException()

    def sync_sql(self):
        conn = SqlConnect()
        conn.connect()
        sql = UpdateTable(db=conn, data=self.data)
        sql.clear_table()
        sql.create()

    def sync_elastic(self):
        conn = ElasticConnect()
        conn.connect()
        i = Index(es=conn.es, data=self.data)
        i.clear_index()
        i.create()
