import scrapy

class AnimenovaSpider(scrapy.Spider):
    name = 'animenova'
    allowed_domains = ['animenova.org']
    start_urls = ['http://animenova.org/anime-list']

    def parse(self, response):
        for href in response.css('#series_grid a::attr("href")').extract():
            yield scrapy.Request(href, self.parse_anime)

    def parse_anime(self, response):
        yield {}

        for href in response.css('#videos a::attr("href")').extract():
            yield scrapy.Request(href, self.parse_episode)

    def parse_episode(self, response):
        yield {}
