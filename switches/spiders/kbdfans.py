import scrapy



class KbdFansScraper(scrapy.Spider):
    name = "kbdfans"
    allowed_domains = ["kbdfans.com"]
    start_urls = [
        "https://kbdfans.com/collections/keycaps"
    ]

    def parse(self, response):
        results = response.xpath('//div[@class="grid-product__content"]')

        for product in results:
            product_name = product.xpath('.//div[@class="grid-product__title"]').extract_first()
            product_url = product.xpath('.//a/@href').extract_first()
            data = {
                "Name": product_name,
                "URL": product_url
            }


            yield data
            # yield scrapy.Request(product_url, meta=data, callback=self.parse_detail_page)

    
    def parse_detail_page(self, response):
        data = response.meta['summary_data']

        # TODO: add more data

        yield data