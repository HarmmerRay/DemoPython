import scrapy


class CatalogSpider(scrapy.Spider):
    name = "catalog"
    allowed_domains = ["3.cn"]
    start_urls = ["https://dc.3.cn/category/get"]

    def parse(self, response):
        print(response)
        pass
