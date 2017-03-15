from scrapy import Spider, Request

from ..loaders import AnimeLoader
from ..items import Anime


class FansubSpider(Spider):
    name = 'fansub'
    allowed_domains = ['fansub.tv']
    start_urls = ['http://fansub.tv/listing.html']

    def parse(self, response):
        for href in response.css('.matv_left a::attr("href")').extract():
            yield Request(response.urljoin(href), self.parse_anime)

    def parse_anime(self, response):
        loader = AnimeLoader(Anime(), response)

        yield loader.load_item()
