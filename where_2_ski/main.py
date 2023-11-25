import scrapy
import logging
from scrapy.crawler import CrawlerProcess

# list to collect all items
items = []

# pipeline to fill the items list
class ItemCollectorPipeline(object):
    def __init__(self):
        self.ids_seen = set()

    def process_item(self, item, spider):
        items.append(item)

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        "https://www.vail.com/the-mountain/mountain-conditions/terrain-and-lift-status.aspx"
    ]

    def parse(self, response):
        yield {
            "trails_open": response.xpath('//*[@id="c118_Terrain_Status_Summary_1"]/div/div[1]/div[2]/div[2]/div[1]/@data-open').extract(),
            "trails_total": response.xpath('//*[@id="c118_Terrain_Status_Summary_1"]/div/div[1]/div[2]/div[2]/div[1]/@data-total').extract()
        }

def main():
    process = CrawlerProcess({
        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
        'LOG_LEVEL': 'INFO',
        'ITEM_PIPELINES': { 'where_2_ski.main.ItemCollectorPipeline': 100 }
    })

    process.crawl(QuotesSpider)
    process.start()

    print(items)

if __name__ == "__main__":
    main()