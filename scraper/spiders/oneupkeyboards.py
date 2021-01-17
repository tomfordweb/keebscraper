import scrapy
from urllib.parse import urljoin
from scraper.items import Product
import sys
"""
TODO: This needs to handle variable products
"""
class OneUpKeyboardsScraper(scrapy.Spider):
    name = "1up"
    allowed_domains = ["1upkeyboards.com"]

    # TODO: Abstract to shared parent spider
    def __init__(self, *args, **kwargs):
        super(OneUpKeyboardsScraper, self).__init__(*args, **kwargs) 

        self.start_urls = [kwargs.get('start_urls', '')]
        self.meta = kwargs.get('meta')

    def parse(self, response):
        # results = response.xpath('//div[@class="grid-product__content"]')
        # TODO: update kbdfans scraper to be more accurate using this better xpath selector now that I understand how this works more
        results = response.xpath("//li[contains(concat(' ', normalize-space(@class),' '),' product ')]")

        for html in results:
            product_url = html.xpath(".//a[contains(concat(' ', normalize-space(@class),' '),' woocommerce-LoopProduct-link ')]/@href").extract_first()
            product = Product()

            # product["category"] = list(self.meta["category"])
            product['name'] = html.xpath(".//*[contains(concat(' ', normalize-space(@class),' '),' woocommerce-loop-product__title ')]/text()").extract_first()
            product['source'] = response.url

            product['price'] = ''.join(html.xpath(".//*[@class='price']/*[last()]/descendant::*/text()").extract())
            
            product['url'] = product_url
            data = {'item': product}
            yield scrapy.Request(product_url, meta=data, callback=self.parse_detail_page)

        next_page_link = response.xpath("//ul[@class='page-numbers']//a[contains(concat(' ', normalize-space(@class), ' '), ' next ')]/@href").extract_first()

        if next_page_link != None:
            yield scrapy.Request(next_page_link, callback=self.parse)

    def parse_detail_page(self, response):
        product = response.meta['item']
        # Woocommerce product meta
        product_meta_html = response.xpath('//*[@class="product_meta"]')
        product['unique_identifier'] = product_meta_html.xpath('//*[@class="sku"]/text()').extract_first()
        product_categories = product_meta_html.xpath('//*[@class="tagged_as"]/a/text()').extract()
        product_tags = product_meta_html.xpath('//*[@class="posted_in"]/a/text()').extract()
        all_categories = product_categories + product_tags
        product['category'] = all_categories
        
        yield product
