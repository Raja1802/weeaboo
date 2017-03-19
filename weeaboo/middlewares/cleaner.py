from lxml.html.clean import Cleaner


class CleanerMiddleware(object):
    def __init__(self):
        self.cleaner = Cleaner(style=True, page_structure=False)

    @classmethod
    def from_crawler(cls, crawler):
        return cls()

    def process_response(self, request, response, spider):
        body = self.cleaner.clean_html(response.body)
        return response.replace(body=body)
