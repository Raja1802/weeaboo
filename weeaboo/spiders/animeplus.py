from scrapy import Spider, Request

from ..loaders import AnimeLoader
from ..items import Anime


class AnimeplusSpider(Spider):
    name = 'animeplus'
    allowed_domains = ['animeplus.tv']
    start_urls = ['http://animeplus.tv/anime-show-list']

    def parse(self, response):
        for href in response.css('.series_index a::attr("href")').extract():
            yield Request(href, self.parse_anime)

    def parse_anime(self, response):
        loader = AnimeLoader(Anime(), response.css('#series_info'))

        loader.add_css('title', 'h1')
        loader.add_xpath('status', '//div[contains(span, "Status")]/text()')
        loader.add_xpath('synopsis', '//span[@id="full_notes"]/text()')
        loader.add_css('image', '#series_image::attr("src")')

        yield loader.load_item()
