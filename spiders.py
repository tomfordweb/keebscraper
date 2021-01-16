import click
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

@click.command()
def runSpiders():
    settings = get_project_settings()
    settings.set('MONGODB_HOST', 'mongo1')
    settings.set('MONGODB_PORT', '27017')
    settings.set('MONGODB_USER', 'root')
    settings.set('MONGODB_PASSWORD', 'example')
    settings.set('MONGODB_DB', 'keebs')
    
    process = CrawlerProcess(settings)
    # process.crawl('ebay-search', search="holy panda mechanical keyboard scraper")
    # process.crawl('ebay-search', search="cherry mx clear")
    # process.crawl('ebay-search', search="cherry mx black")

    process.crawl('kbdfans', url="https://kbdfans.com/collections/cherry-profile")
    process.crawl('kbdfans', url="https://kbdfans.com/collections/sa-profile")
    process.crawl('kbdfans', url="https://kbdfans.com/collections/dsa-profile")
    process.crawl('kbdfans', url="https://kbdfans.com/collections/mix-profile")
    process.crawl('kbdfans', url="https://kbdfans.com/collections/kat-profile")
    process.crawl('kbdfans', url="https://kbdfans.com/collections/np-profile")
    process.crawl('kbdfans', url="https://kbdfans.com/collections/da-profile")
    process.crawl('kbdfans', url="https://kbdfans.com/collections/electrostatic-capacitive-keycaps")
    process.crawl('kbdfans', url="https://kbdfans.com/collections/oem-profile")
    process.crawl('kbdfans', url="https://kbdfans.com/collections/osa-profile")
    process.crawl('kbdfans', url="https://kbdfans.com/collections/enjoypbt-keycaps")
    process.crawl('kbdfans', url="https://kbdfans.com/collections/maxkey")
    process.crawl('kbdfans', url="https://kbdfans.com/collections/artisan-keycaps")
    process.crawl('kbdfans', url="https://kbdfans.com/collections/backlit-keycaps")
    process.crawl('kbdfans', url="https://kbdfans.com/collections/aliaz-switches")
    process.crawl('kbdfans', url="https://kbdfans.com/collections/cherry-switches")
    process.crawl('kbdfans', url="https://kbdfans.com/collections/gateron-swithes")
    process.crawl('kbdfans', url="https://kbdfans.com/collections/kailh-switches")
    process.crawl('kbdfans', url="https://kbdfans.com/collections/switches-tester")
    process.crawl('kbdfans', url="https://kbdfans.com/collections/zealios-switches")
    process.start()

if __name__ == '__main__':
    runSpiders()
