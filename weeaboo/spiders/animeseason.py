from scrapy import Spider, Request

from ..loaders import AnimeLoader
from ..items import Anime


class AnimeseasonSpider(Spider):
    name = 'animeseason'
    allowed_domains = ['animeseason.com']
    start_urls = ['http://animeseason.com/anime-list']

    def parse(self, response):
        for href in response.css('ul.series_alpha a::attr("href")').extract():
            yield Request(response.urljoin(href), self.parse_anime)

    def parse_anime(self, response):
        loader = AnimeLoader(Anime(), response)

        yield loader.load_item()
