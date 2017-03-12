import sqlite3

class StoragePipeline(object):
    def __init__(self, filename):
        self.filename = filename

    @classmethod
    def from_crawler(cls, crawler):
        return cls (
            filename = crawler.settings.get('BOT_NAME') + '.db',
        )

    def open_spider(self, spider):
        self.con = sqlite3.connect(self.filename)
        self.cur = self.con.cursor()

    def close_spider(self, spider):
        self.con.close()

    def process_item(self, item, spider):
        anime = (
           item['title'],
           item['status'],
           item['synopsis'],
           item['image']
        )
        self.cur.execute("INSERT INTO anime VALUES (?, ?, ?, ?)", anime)
        self.con.commit()
        return item