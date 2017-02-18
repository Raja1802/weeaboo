# -*- coding: utf-8 -*-
import scrapy


class AnimeseasonSpider(scrapy.Spider):
    name = "animeseason"
    allowed_domains = ["animeseason.com"]
    start_urls = ['http://animeseason.com/']

    def parse(self, response):
        pass
