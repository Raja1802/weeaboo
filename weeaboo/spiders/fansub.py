import scrapy

class FansubSpider(scrapy.Spider):
    name = 'fansub'
    allowed_domains = ['fansub.tv']
    start_urls = ['http://fansub.tv/listing.html']

    def parse(self, response):
        for href in response.css('.matv_left a::attr("href")').extract():
            yield scrapy.Request(response.urljoin(href), self.parse_anime)

    def parse_anime(self, response):
        yield {}

        for href in response.css('.matv_center a::attr("href")').extract():
            yield scrapy.Request(response.urljoin(href), self.parse_episode)

    def parse_episode(self, response):
        yield {}
