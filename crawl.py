import click
import scrapy
import sys
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from os import path
import json


def metaFactory(currentCrawlData: dict, jobData: dict):
    accessibleMeta = {
        "category": []
    }
    sharedMeta = jobData.get('meta', accessibleMeta)
    crawlMeta = currentCrawlData.get('meta', accessibleMeta)

    return {
        "category": sharedMeta.get('category', []) + crawlMeta.get('category', []) 
    }

@click.command()
@click.option('--file', '-f', multiple=True, required=True)
def runSpiders(file):
    files = file

    for settingFile in files:
        if False == path.isfile(f"/app/crawls/{settingFile}.json"):
            raise IOError(f"Invalid Setting {settingFile} ")
    
    settings = get_project_settings()
    process = CrawlerProcess(settings)

    for job in files:
        with open(f"/app/crawls/{job}.json") as f:
            data = json.load(f)
            crawler = data['job']
            shared_meta = data['meta']

            for crawl in data['crawls']:
                process.crawl(
                    crawl['spider'],
                    start_urls=crawl['url'],
                    meta=metaFactory(crawl, data)
                )

    process.start()

if __name__ == '__main__':
    runSpiders()
