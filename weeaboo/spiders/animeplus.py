from scrapy import Spider, Request

class AnimeplusSpider(Spider):
    name = 'animeplus'
    allowed_domains = ['animeplus.tv']
    start_urls = ['http://animeplus.tv/anime-show-list']

    def parse(self, response):
        for href in response.css('.series_index a::attr("href")').extract():
            yield Request(href, self.parse_anime)

    def parse_anime(self, response):
        yield {}

        for href in response.css('#videos a::attr("href")').extract():
            yield Request(href, self.parse_episode)

    def parse_episode(self, response):
        yield {}
