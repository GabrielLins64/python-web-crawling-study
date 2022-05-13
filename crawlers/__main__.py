from .urllib_crawler import UrlLibCrawler


SOURCES = [
    'https://filipedeschamps.com.br/',
]


if __name__ == '__main__':
    crawler = UrlLibCrawler(SOURCES)
    crawler.dig()
