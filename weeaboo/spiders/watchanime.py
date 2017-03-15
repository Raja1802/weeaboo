from scrapy import Spider, Request

from ..loaders import AnimeLoader
from ..items import Anime


class WatchanimeSpider(Spider):
    name = 'watchanime'
    allowed_domains = ['watchanime.com']
    start_urls = ['http://watchanime.com/anime-list']

    def parse(self, response):
        for href in response.css('.panel-body a::attr("href")').extract():
            yield Request(href, self.parse_anime)

    def parse_anime(self, response):
        loader = AnimeLoader(Anime(), response)

        yield loader.load_item()
