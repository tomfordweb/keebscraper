import click
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

@click.command()
def runSpiders():
    process = CrawlerProcess(get_project_settings())
    process.crawl('ebay-switches', search="holy panda mechanical keyboard switches")
    process.crawl('ebay-switches', search="cherry mx clear")
    process.crawl('ebay-switches', search="cherry mx black")
    process.start()

if __name__ == '__main__':
    runSpiders()
