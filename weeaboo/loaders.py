from w3lib.html import remove_tags, strip_html5_whitespace

from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, TakeFirst

class AnimeLoader(ItemLoader):
    default_input_processor = MapCompose(remove_tags, strip_html5_whitespace)
    default_output_processor = TakeFirst()

    status_in = category_in = MapCompose(remove_tags, strip_html5_whitespace, str.lower)
