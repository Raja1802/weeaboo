from scrapy import Item, Field

class Anime(Item):
    title = Field()
    category = Field()
    status = Field()
    synopsis = Field()
    image = Field()
