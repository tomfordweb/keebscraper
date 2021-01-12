import scrapy
from urllib.parse import urljoin

"""
Notes:
- kbdfans uses absolute urls in their website structure, sou you need to join url's together using urljoin
- like most sites, they show the sold out and historical products, so we are excluding sold and ended group buys.
"""
class KbdFansScraper(scrapy.Spider):
    name = "kbdfans"
    allowed_domains = ["kbdfans.com"]
    start_urls = [
        "https://kbdfans.com/collections/keycaps"
    ]

    ignored_product_statuses = [
        "Sold Out"
    ]

    ignored_product_title_contains = [
        "[IC]", # Interest check
    ]
    def parse(self, response):
        results = response.xpath('//div[@class="grid-product__content"]')
        title = response.xpath('//title/text()').extract_first().strip()

        for product in results:
            product_badge = product.xpath('./div/text()').extract_first(default="Active").strip()
            product_name = product.xpath('.//div[@class="grid-product__title"]/text()').extract_first().strip()


            if product_badge not in self.ignored_product_statuses and not any(match in product_name for match in self.ignored_product_title_contains):
                product_url = product.xpath('.//a/@href').extract_first()
                product_url = urljoin(response.url, product_url)
                summary_data = {
                    "Category": title,
                    "Name": product_name,
                    "URL": product_url
                }
                
                data = {'summary_data': summary_data}
                yield scrapy.Request(product_url, meta=data, callback=self.parse_detail_page)

        # # Process pagination links 
        next_page_link = response.xpath("//div[@class='pagination']//span[@class='next']/a/@href").extract_first()
        next_page_link = urljoin(response.url, next_page_link)

        if next_page_link != None:
            yield scrapy.Request(next_page_link, callback=self.parse)

    def parse_detail_page(self, response):
        data = response.meta['summary_data']

        sku = response.xpath('//p[@class="product-single__sku"]/text()').extract_first(default="N/A").strip()
        price = response.xpath('//span[@class="product__price"]/text()').extract_first(default="N/A").strip()

        data["SKU"] = sku
        data["Price"] = price

        # TODO: add more data

        yield data