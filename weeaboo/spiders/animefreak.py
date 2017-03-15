from scrapy import Spider, Request

from ..loaders import AnimeLoader
from ..items import Anime


class AnimefreakSpider(Spider):
    name = 'animefreak'
    allowed_domains = ['animefreak.tv']
    start_urls = ['http://animefreak.tv/book']

    def parse(self, response):
        for href in response.css('.singlepage .item-list a::attr("href")').extract():
            yield Request(response.urljoin(href), self.parse_anime)

    def parse_anime(self, response):
        loader = AnimeLoader(Anime(), response)

        yield loader.load_item()
