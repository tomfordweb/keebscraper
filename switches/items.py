# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class Product(scrapy.Item):
    name = Field()
    price = Field()
    source = Field()
    url = Field()
    status = Field()
    
class EbayProduct(Product):
    stars = Field()
    ratings = Field()


class SwitchesItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
