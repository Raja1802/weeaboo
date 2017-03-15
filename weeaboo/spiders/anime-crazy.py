from scrapy import Spider, Request

from ..loaders import AnimeLoader
from ..items import Anime


class AnimecrazySpider(Spider):
    name = 'anime-crazy'
    allowed_domains = ['anime-crazy.org']
    start_urls = ['http://anime-crazy.org/animelist']

    def parse(self, response):
        for href in response.css('[width="99%"] a::attr("href")').extract():
            yield Request(href, self.parse_anime)

    def parse_anime(self, response):
        loader = AnimeLoader(Anime(), response)

        yield loader.load_item()
