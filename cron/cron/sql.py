class UpdateTable:
    def __init__(self, db, data):
        self.db = db
        self.data = data
        self.table_name = "search_pypipackage"

    def clear_table(self):
        if self.data:
            self.db.cursor.execute(f"DELETE FROM {self.table_name}")
            self.db.conn.commit()

    def create(self):
        if self.data:
            for i in self.data:
                db_data = (
                    i.get("title"),
                    i['author'] or "undefined",
                    i["description"],
                    i["link"],
                    i["version"],
                    i['authors'] or "undefined"
                )
                self.db.cursor.execute(
                    f"INSERT INTO {self.table_name}('title', 'author', 'description', 'link', 'version', 'authors') "
                    f"VALUES (? ,?,?,?,?,?)", db_data)
                self.db.conn.commit()
