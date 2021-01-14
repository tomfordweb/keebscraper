import scrapy
from itemloaders.processors import Join, MapCompose, TakeFirst
from w3lib.html import remove_tags

class Product(scrapy.Item):
    scraper_source = scrapy.Field()
    name = scrapy.Field()
    price = scrapy.Field()
    source = scrapy.Field()
    url = scrapy.Field()
    status = scrapy.Field()
    unique_identifier = scrapy.Field()
    
class EbayProduct(Product):
    stars = scrapy.Field()
    ratings = scrapy.Field()

class ScraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
