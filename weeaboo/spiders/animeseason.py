import scrapy

class AnimeseasonSpider(scrapy.Spider):
    name = 'animeseason'
    allowed_domains = ['animeseason.com']
    start_urls = ['http://animeseason.com/anime-list']

    def parse(self, response):
        for href in response.css('ul.series_alpha a::attr("href")').extract():
            yield scrapy.Request(response.urljoin(href), self.parse_anime)

    def parse_anime(self, response):
        print(response)
