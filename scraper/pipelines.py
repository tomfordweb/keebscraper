from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem
from elasticsearch import Elasticsearch
import hashlib

class ElasticsearchPipeline:
    COLLECTION_NAME = 'products'

    def __init__(self):
        self.es = Elasticsearch(
            ["es01","es02","es03"]
        )

    def process_item(self, item, spider):
        self.es.index(index=self.COLLECTION_NAME, id=urlHash, body=dict(item))

class ProductPipeline:
    def process_item(self, item, spider):
        # Create a unique ID of the product so we can keep it up to date.
        item['id'] = hashlib.md5(item['url'].encode()).hexdigest()

        return item


class KbdFansPipeline:
    ignored_product_statuses = [
        # "Sold Out"
    ]

    ignored_product_title_contains = [
    ]
    def process_item(self, item, spider):
        # Only handle items scraped from kbdfans
        if spider.name != "kbdfans":
            return item

        if item['status'] in self.ignored_product_statuses:
            raise DropItem(f"Item {item['name']} dropped due to status {item['status']}")

        if any(match in item['name'] for match in self.ignored_product_title_contains):
            raise DropItem(f"Item has ignored string in title")

        item['scraper_source'] = spider.name
        return item

