from scrapy import Item, Field

class Anime(Item):
    title = Field()
    alt_titles = Field()
    category = Field()
    status = Field()
    genres = Field()
    image = Field()
    synopsis = Field()

class Episode(Item):
    number = Field()
    title = Field()
