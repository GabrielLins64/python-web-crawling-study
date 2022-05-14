import scrapy
from scrapy.crawler import CrawlerProcess


class ScrapyCrawler(scrapy.Spider):
    """Scrapy Web Crawler"""


    def __init__(self):
        self.start_urls = ["https://quotes.toscrape.com/page/1",
                           "https://quotes.toscrape.com/page/2",]
        super().__init__(name="Quotes Spider")


    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f'data/quotes-{page}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')


    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse)


    @classmethod
    def dig(cls):
        process = CrawlerProcess({
            'USER_AGENT': 'Mozilla/5.0'
        })

        process.crawl(cls)
        process.start()
