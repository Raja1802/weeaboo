from scrapy import Spider, Request

class WatchanimeSpider(Spider):
    name = 'watchanime'
    allowed_domains = ['watchanime.com']
    start_urls = ['http://watchanime.com/anime-list']

    def parse(self, response):
        for href in response.css('.panel-body a::attr("href")').extract():
            yield Request(href, self.parse_anime)

    def parse_anime(self, response):
        yield {}

        for href in response.css('.entry-title a::attr("href")').extract():
            yield Request(href, self.parse_episode)

    def parse_episode(self, response):
        yield {}
