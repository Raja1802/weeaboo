from scrapy import Spider, Request

class AnilinkzSpider(Spider):
    name = 'anilinkz'
    allowed_domains = ['anilinkz.io']
    start_urls = ['http://anilinkz.io/anime-list']

    def parse(self, response):
        for href in response.css('.se a::attr("href")').extract():
            yield Request(response.urljoin(href), self.parse_anime)

    def parse_anime(self, response):
        yield {}

        for href in response.css('.epser > a::attr("href")').extract():
            yield Request(response.urljoin(href), self.parse_episode)

    def parse_episode(self, response):
        yield {}
