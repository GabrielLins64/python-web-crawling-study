from urllib.request import Request, urlopen
from . import Crawler
import re


class UrlLibCrawler(Crawler):
    """urllib Web Crawler"""

    def __init__(self, sources: list = []):
        super().__init__(sources)
        self.headers = {
            'User-Agent': 'Mozilla/5.0'
        }

    def dig(self):
        result = dict()
        for source in self.sources:
            req = Request(source['url'],
                          headers=self.headers)
            html = urlopen(req).read()
            html = str(html)

            for data in source['data']:
                regex = re.search(data['find_regex'], html)
                regex_result = \
                    regex.group(1) if hasattr(regex, "groups") else "Not found"
                result[data['result_name']] = regex_result

        return result
