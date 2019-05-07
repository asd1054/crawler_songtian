
"""
    requests                和            scrapy       的区别
    页面级爬虫                           网站级爬虫
    功能库                               框架
    并发性考虑不足，性能较差             并发性好，性能较高
    重点在于页面下载                    重点在于爬虫结构
    定制灵活                            一般定制灵活，深度定制困难
    上手十分简单                        相对来说，比较困难



    非常小的需求 ，    requests库
    不太小的需求 ，    scrapy框架
    定制成都很高的需求（不考虑规模），自搭框架， requests  >  scrapy



"""

# -*- coding: utf-8 -*-
import scrapy
class DemoSpider(scrapy.Spider):
    name = "demo"
    #allowed_domains = ["python123.io"]
    def start_requests(self):    
        start_urls = [
            'http://python123.io/ws/demo.html'
            ]
        for url in start_urls:
            yield scrapy.Request(url=url,callback = self.parse)
    def parse(self, response):
        fname = response.url.split('/')[-1]
        with open(fname, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s.' % name)
        pass

    def main(self):
        urls = start_requests()
        for i in urls:
            parse(i)
    

a = DemoSpider()
a.main()