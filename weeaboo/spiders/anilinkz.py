from scrapy import Spider, Request

from ..loaders import AnimeLoader
from ..items import Anime

class AnilinkzSpider(Spider):
    name = 'anilinkz'
    allowed_domains = ['anilinkz.io']
    start_urls = ['http://anilinkz.io/anime-list']

    def parse(self, response):
        for href in response.css('.se a::attr("href")').extract():
            yield Request(response.urljoin(href), self.parse_anime)

    def parse_anime(self, response):
        loader = AnimeLoader(Anime(), response)



        yield loader.load_item()
