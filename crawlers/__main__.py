from .urllib_crawler import UrlLibCrawler
from pprint import pprint
import json


SEARCH_FILE = "search.json"


if __name__ == '__main__':
    with open(SEARCH_FILE) as f:
        sources = json.loads(f.read())

    crawler = UrlLibCrawler(sources)
    result = crawler.dig()

    pprint(result)
