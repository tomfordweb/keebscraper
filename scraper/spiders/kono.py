import scrapy
from urllib.parse import urljoin
from scraper.items import Product
import sys

class KonoScraper(scrapy.Spider):
    name = "kono"
    allowed_domains = ["kono.store"]

    # TODO: Abstract to shared parent spider
    def __init__(self, *args, **kwargs):
        super(KonoScraper, self).__init__(*args, **kwargs) 

        self.start_urls = [kwargs.get('start_urls', '')]
        self.meta = kwargs.get('meta')

    def parse(self, response):
        results = response.xpath("//li[contains(concat(' ', normalize-space(@class),' '),' productgrid--item ')]")
        for html in results:
            product_url = html.xpath(".//a/@href").extract_first()
            product = Product()
            product['name'] = html.xpath('.//h2[@class="productitem--title"]/descendant::*/text()').extract_first().strip()

            product['source'] = response.url

            price = html.xpath(".//*[@class='price--main']/text()").extract_first().strip()

            if len(price) == 0:
                price = html.xpath(".//*[@class='price--main']/span[@class='money']/text()").extract_first().strip()

            product['price'] = price

            product['category'] = html.xpath(".//span[contains(concat(' ', normalize-space(@class), ' '), ' productitem--badge ')]/text()").extract_first(default="N/A").strip()

            product['url'] = product_url
            yield product



