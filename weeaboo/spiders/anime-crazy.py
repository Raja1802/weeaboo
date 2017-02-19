import scrapy

class AnimeCrazySpider(scrapy.Spider):
    name = 'anime-crazy'
    allowed_domains = ['anime-crazy.org']
    start_urls = ['http://anime-crazy.org/animelist']

    def parse(self, response):
        for href in response.css('.hover-table a::attr("href")').extract():
            yield scrapy.Request(href, self.parse_anime)

    def parse_anime(self, response):
        yield {}

        for href in response.css('#epi_ul a::attr("href")').extract():
            yield scrapy.Request(href, self.parse_episode)

    def parse_episode(self, response):
        yield {}
