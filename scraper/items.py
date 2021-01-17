import scrapy
from itemloaders.processors import Join, MapCompose, TakeFirst
# additional scraping ideas
# The payment methods on the product page
# Process the product description for tags and categories, but do not save it.

class Product(scrapy.Item):
    id = scrapy.Field()
    scraper_source = scrapy.Field()
    name = scrapy.Field()
    price = scrapy.Field()
    source = scrapy.Field()
    url = scrapy.Field()
    status = scrapy.Field()
    category = scrapy.Field()
    unique_identifier = scrapy.Field()
    description = scrapy.Field()
