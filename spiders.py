import click
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

@click.command()
def runSpiders():
    process = CrawlerProcess(get_project_settings())
    # process.crawl('ebay-search', search="holy panda mechanical keyboard scraper")
    # process.crawl('ebay-search', search="cherry mx clear")
    process.crawl('ebay-search', search="cherry mx black")
    # process.crawl('kbdfans', url="https://kbdfans.com/collections/60-layout-plate-1")
    process.start()

if __name__ == '__main__':
    runSpiders()
