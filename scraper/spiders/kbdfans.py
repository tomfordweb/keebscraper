import scrapy
from urllib.parse import urljoin
from scraper.items import Product
import sys

class KbdFansScraper(scrapy.Spider):
    name = "kbdfans"
    allowed_domains = ["kbdfans.com"]

    def __init__(self, *args, **kwargs):
        super(KbdFansScraper, self).__init__(*args, **kwargs) 

        self.start_urls = [kwargs.get('start_urls', '')]
        self.meta = kwargs.get('meta')

    def parse(self, response):
        results = response.xpath('//div[@class="grid-product__content"]')

        for html in results:
            # shopify uses absolute urls
            product_url = html.xpath('.//a/@href').extract_first()
            product_url = urljoin(response.url, product_url)

            product = Product()

            product["category"] = list(self.meta["category"])

            product['name'] = html.xpath('.//div[@class="grid-product__title"]/text()').extract_first(default="N/A").strip()
            product['source'] = response.url
            product['url'] = product_url
            product['status'] = html.xpath('./div/text()').extract_first(default="N/A").strip()
            # data = {'item': product}
            yield product
        #     yield scrapy.Request(product_url, meta=data, callback=self.parse_detail_page)

        # next_page_link = response.xpath("//div[@class='pagination']//span[@class='next']/a/@href").extract_first()
        # next_page_link = urljoin(response.url, next_page_link)

        # if next_page_link != None:
        #     yield scrapy.Request(next_page_link, callback=self.parse)

    def parse_detail_page(self, response):
        product = response.meta['item']

        sku = response.xpath('//p[@class="product-single__sku"]/text()').extract_first(default="N/A").strip()
        price = response.xpath('//span[@class="product__price"]/text()').extract_first(default="N/A").strip()

        product["unique_identifier"] = sku
        product["price"] = price


        yield product