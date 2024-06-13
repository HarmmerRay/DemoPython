import json

import scrapy


class CatalogSpider(scrapy.Spider):
    name = 'catalog'
    allowed_domains = ['3.cn']
    start_urls = ['https://dc.3.cn/category/get']

    def parse(self, response):
        catalog_json = json.loads(str(response.body, 'gbk'))
        result = []
        for item in catalog_json['data']:

            for data1 in item['s']:
                url1 = data1['n'].split("|")[0]
                str1 = data1['n'].split("|")[1]
                result1 = {
                    'url': url1,
                    'title': str1,
                    'child': []
                }
                result.append(result1)

                for data2 in data1['s']:
                    url2 = data2['n'].split("|")[0]
                    str2 = data2['n'].split("|")[1]
                    result2 = {
                        'url': url2,
                        'title': str2,
                        'child': []
                    }
                    result1.get('child').append(result2)

                    for data3 in data2['s']:
                        url3 = data3['n'].split("|")[0]
                        str3 = data3['n'].split("|")[1]
                        result3 = {
                            'url': url3,
                            'title': str3,
                        }
                        result2.get('child').append(result3)
        print(result)
    pass
