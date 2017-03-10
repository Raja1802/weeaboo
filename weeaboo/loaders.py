from scrapy.loader import ItemLoader
from scrapy.loader.processors import Identity, MapCompose, TakeFirst

from w3lib.html import remove_tags, strip_html5_whitespace

class AnimeLoader(ItemLoader):
    default_input_processor = MapCompose(remove_tags, strip_html5_whitespace)
    default_output_processor = TakeFirst()

    alt_titles_out = MapCompose(lambda v: v.split(','))
    genres_out = Identity()
