from bs4 import BeautifulSoup


class BeautifulSoupMiddleware(object):
    def __init__(self, settings):
        self.parser = settings.get('BEAUTIFULSOUP_PARSER', 'html.parser')

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.settings)

    def process_response(self, request, response, spider):
        body = str(BeautifulSoup(response.body, self.parser))
        return response.replace(body=body)
