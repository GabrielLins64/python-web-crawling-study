from .urllib_crawler import UrlLibCrawler
from .scrapy_crawler import ScrapyCrawler
from pprint import pprint
import json


SEARCH_FILE = "search.json"


def test_urrlib_crawler():
    with open(SEARCH_FILE) as f:
        sources = json.loads(f.read())

    crawler = UrlLibCrawler(sources)
    result = crawler.dig()

    pprint(result)


def test_scrapy_crawler():
    ScrapyCrawler.dig()


if __name__ == '__main__':
    # test_urrlib_crawler()
    test_scrapy_crawler()
