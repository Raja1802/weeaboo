import sqlite3

from scrapy.commands import ScrapyCommand
from scrapy.exceptions import UsageError

class Command(ScrapyCommand):

    requires_project = True
    default_settings = {'LOG_ENABLED': False}

    def syntax(self):
        return '<action>'

    def short_desc(self):
        return 'Manage the database'

    def run(self, args, opts):
        if len(args) != 1:
            raise UsageError()

        con = sqlite3.connect(self.crawler_process.settings.get('DATABASE_URL'), uri=True)
        cur = con.cursor()

        if args[0] == 'create':
            cur.execute('''CREATE TABLE IF NOT EXISTS anime (
                id INTEGER PRIMARY KEY,
                title TEXT NOT NULL,
                category TEXT NOT NULL DEFAULT series,
                status TEXT,
                synopsis TEXT,
                image TEXT
            )''')
        elif args[0] == 'drop':
            cur.execute('DROP TABLE IF EXISTS anime')

        con.commit()
        con.close()
