<h1>Study of Web Crawlers in Python</h1>

A web crawler, or *web spider*, refers to a bot that searches data on the web. Basically, web crawlers are mindful for understanding the substance on a web page so they can recover it when an request is made.

---

<h2>Index</h2>

- [Dependencies](#dependencies)
- [Installation](#installation)
- [Crawlers](#crawlers)
  - [Urllib](#urllib)
  - [Scrapy](#scrapy)
    - [Starting a scrapy project](#starting-a-scrapy-project)
    - [Running the scrapy project](#running-the-scrapy-project)
  - [Selenium](#selenium)

---

## Dependencies

- Python 3

## Installation

1. Create a python virtual environment and activate it

```sh
python3 -m venv venv
source venv/bin/activate
```

2. Install dependencies

```sh
python -m pip install -r requirements.txt
```

## Crawlers

- [X] urllib crawlers
- [X] Scrapy crawlers
- [ ] Selenium crawlers

### Urllib

### Scrapy

[Official docs](https://docs.scrapy.org/en/latest/index.html)

#### Starting a scrapy project

Create a new scrapy project:

```shell
scrapy startproject scrapy_crawlers_proj
```

#### Running the scrapy project

In order to run the named "*quotes*" spider, defined at `scrapy_crawlers_proj/spiders/quotes_spider.py`, simply run:

```shell
scrapy crawl quotes
```

### Selenium
