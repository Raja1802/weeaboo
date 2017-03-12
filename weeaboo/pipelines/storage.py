import sqlite3

class StoragePipeline(object):
    def __init__(self, database_url):
        self.database_url = database_url

    @classmethod
    def from_crawler(cls, crawler):
        return cls(database_url=crawler.settings.get('DATABASE_URL'))

    def open_spider(self, spider):
        self.con = sqlite3.connect(self.database_url, uri=True)
        self.cur = self.con.cursor()

    def close_spider(self, spider):
        self.con.close()

    def process_item(self, item, spider):
        columns = ', '.join(item.keys())
        placeholders = ':' + ', :'.join(item.keys())
        query = 'INSERT INTO anime ({}) VALUES ({})'.format(columns, placeholders)

        self.cur.execute(query, dict(item))
        self.con.commit()

        return item
