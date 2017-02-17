from scrapy import signals

class WeeabooSpiderMiddleware(object):
    @classmethod
    def from_crawler(cls, crawler):
        """Creates spiders."""

        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(response, spider):
        """Called for each response that goes through the spider middleware and into the spider."""

        return None

    def process_spider_output(response, result, spider):
        """Called with the results returned from the Spider, after processing the response."""

        for i in result:
            yield i

    def process_spider_exception(response, exception, spider):
        """Called when a spider raises an exception."""

        pass

    def process_start_requests(start_requests, spider):
        """Called with the start requests of the spider."""

        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
