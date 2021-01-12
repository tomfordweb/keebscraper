# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem


class ScraperItemPipeline:
    def process_item(self, item, spider):
        return item


class KbdFansPipeline:
    ignored_product_statuses = [
        "Sold Out"
    ]

    ignored_product_title_contains = [
        "[IC]", # Interest check
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