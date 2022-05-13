from urllib import request
from . import Crawler


class UrlLibCrawler(Crawler):
    """urllib Web Crawler"""

    def __init__(self, sources: list = []):
        super().__init__(sources)

    def dig(self):
        for source in self.sources:
            html = request.urlopen(source).read()
            print(html)
