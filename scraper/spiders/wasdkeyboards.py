
import scrapy
from urllib.parse import urljoin
from scraper.items import Product
import sys

class WasdKeyboardsScraper(scrapy.Spider):
    """
    NOTE: This website is pretty hard to scrape, it is difficult to get data from the product pages so it is left out for now.
    """
    name = "wasd"
    allowed_domains = ["wasdkeyboards.com"]

    # TODO: Abstract to shared parent spider
    def __init__(self, *args, **kwargs):
        super(WasdKeyboardsScraper, self).__init__(*args, **kwargs) 

        self.start_urls = [kwargs.get('start_urls', '')]
        self.meta = kwargs.get('meta')

    def parse(self, response):
        results = response.xpath("//li[contains(concat(' ', normalize-space(@class),' '),' product ')]")

        for html in results:
            product_url = html.xpath(".//a/@href").extract_first()
            product = Product()

            # product["category"] = list(self.meta["category"])
            product['name'] = html.xpath(".//*[contains(concat(' ', normalize-space(@class),' '),' product-item-name ')]/descendant::*/text()").extract_first().strip()
            product['source'] = response.url

            product['price'] = ''.join(html.xpath(".//span[@class='price']/text()").extract())
            
            product['url'] = product_url
            data = {'item': product}

            yield product
