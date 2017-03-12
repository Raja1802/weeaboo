import sqlite3

from scrapy.commands import ScrapyCommand
from scrapy.exceptions import UsageError

class Command(ScrapyCommand):

    requires_project = True

    def syntax(self):
        return '<action>'

    def short_desc(self):
        return 'Manage the database'

    def run(self, args, opts):
        if len(args) != 1:
            raise UsageError()

        con = sqlite3.connect(self.crawler_process.settings['DATABASE_URL'], uri=True)
        cur = con.cursor()

        if args[0] == 'create':
            cur.execute('''CREATE TABLE IF NOT EXISTS anime (
                id integer PRIMARY KEY,
                title text NOT NULL,
                category text NOT NULL DEFAULT series,
                status text,
                synopsis text,
                image text
            )''')
        elif args[0] == 'drop':
            cur.execute('DROP TABLE IF EXISTS anime')

        con.commit()
        con.close()
