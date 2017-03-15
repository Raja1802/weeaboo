from scrapy import Spider, Request

from ..loaders import AnimeLoader
from ..items import Anime


class AnimenovaSpider(Spider):
    name = 'animenova'
    allowed_domains = ['animenova.org']
    start_urls = ['http://animenova.org/anime-list']

    def parse(self, response):
        for href in response.css('#series_grid a::attr("href")').extract():
            yield Request(href, self.parse_anime)

    def parse_anime(self, response):
        loader = AnimeLoader(Anime(), response)

        yield loader.load_item()
