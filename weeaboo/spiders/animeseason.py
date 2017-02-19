from scrapy import Spider, Request

class AnimeseasonSpider(Spider):
    name = 'animeseason'
    allowed_domains = ['animeseason.com']
    start_urls = ['http://animeseason.com/anime-list']

    def parse(self, response):
        for href in response.css('ul.series_alpha a::attr("href")').extract():
            yield Request(response.urljoin(href), self.parse_anime)

    def parse_anime(self, response):
        yield {}

        for href in response.css('.content_bloc > table td:first-child a::attr("href")').extract():
            yield Request(response.urljoin(href), self.parse_episode)

    def parse_episode(self, response):
        yield {}
