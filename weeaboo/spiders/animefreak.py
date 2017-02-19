from scrapy import Spider, Request

class AnimefreakSpider(Spider):
    name = 'animefreak'
    allowed_domains = ['animefreak.tv']
    start_urls = ['http://animefreak.tv/book']

    def parse(self, response):
        for href in response.css('.singlepage .item-list a::attr("href")').extract():
            yield Request(response.urljoin(href), self.parse_anime)

    def parse_anime(self, response):
        yield {}

        for href in response.css('.book-navigation .menu a::attr("href")').extract():
            yield Request(response.urljoin(href), self.parse_episode)

    def parse_episode(self, response):
        yield {}
