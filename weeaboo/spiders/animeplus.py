from scrapy import Spider, Request
from scrapy.loader import ItemLoader

from ..items import Anime

class AnimeplusSpider(Spider):
    name = 'animeplus'
    allowed_domains = ['animeplus.tv']
    start_urls = ['http://animeplus.tv/anime-show-list']

    def parse(self, response):
        for href in response.css('.series_index a::attr("href")').extract():
            yield Request(href, self.parse_anime)

    def parse_anime(self, response):
        loader = ItemLoader(Anime(), response.css('#series_info'))

        loader.add_css('title', 'h1')
        loader.add_css('alt_titles', 'span:contains("Titles") ~ div')
        loader.add_css('category', 'span:contains("Category") ~ a')
        loader.add_xpath('status', '//div[./span[contains(.,"Status")]]')
        loader.add_css('genres', '.red_box a')
        loader.add_css('image', '#series_image')
        loader.add_css('synopsis', 'span:contains("Description") ~ div')

        yield loader.load_item()

        """
        for href in response.css('#videos a::attr("href")').extract():
            yield Request(href, self.parse_episode)
        """

    def parse_episode(self, response):
        yield {}
