"""
    步骤1： 建立工程和Spider模板
                scrapy startproject BaiduStocks
                cd BaiduStocks
                scrapy genspider stocks baidu.com
                进一步修改spiders/stocks.py文件
    步骤2： 编写Spider
                配置stocks.py文件
                修改对返回页面的处理
                修改对新增URL爬取请求的处理
    步骤3： 编写ITEM Pipeline
                

"""


# -*- coding: utf-8 -*-
import scrapy
import re
 
 
class StocksSpider(scrapy.Spider):
    name = "stocks"
    start_urls = ['http://quote.eastmoney.com/stocklist.html']
 
    def parse(self, response):
        for href in response.css('a::attr(href)').extract(): #extract 只处理正确的数据
            try:
                stock = re.findall(r"[s][hz]\d{6}", href)[0]
                url = 'http://gupiao.baidu.com/stock/' + stock + '.html'
                yield scrapy.Request(url, callback=self.parse_stock)
            except:
                continue
 
    def parse_stock(self, response):
        infoDict = {}
        stockInfo = response.css('.stock-bets')
        name = stockInfo.css('.bets-name').extract()[0]
        keyList = stockInfo.css('dt').extract()
        valueList = stockInfo.css('dd').extract()
        for i in range(len(keyList)):
            key = re.findall(r'>.*</dt>', keyList[i])[0][1:-5]
            try:
                val = re.findall(r'\d+\.?.*</dd>', valueList[i])[0][0:-5]
            except:
                val = '--'
            infoDict[key]=val
 
        infoDict.update(
            {'股票名称': re.findall('\s.*\(',name)[0].split()[0] + \
             re.findall('\>.*\<', name)[0][1:-1]})
        yield infoDict


# -*- coding: utf-8 -*-
 
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
 
 
class BaidustocksPipeline(object):
    def process_item(self, item, spider):
        return item
 
class BaidustocksInfoPipeline(object):
    def open_spider(self, spider):
        self.f = open('BaiduStockInfo.txt', 'w')
 
    def close_spider(self, spider):
        self.f.close()
 
    def process_item(self, item, spider):
        try:
            line = str(dict(item)) + '\n'
            self.f.write(line)
        except:
            pass
        return item


# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'BaiduStocks.pipelines.BaidustocksInfoPipeline': 300,
}