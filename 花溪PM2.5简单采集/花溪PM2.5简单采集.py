#encoding = 'utf-8'
import requests

#没有用到，网络太卡了，没有看该视频
from bs4 import BeautifulSoup as bs

#用来记录时间
from datetime import datetime

import re

#PM2.5环境判断
def pm(PM):
    #PM = eval (input("请输入PM2.5数值："))
    if (0<= PM <35):
        print("今天花溪",PM,"PM2.5")
        print("空气优质，快去户外运动！")
    elif 35<=PM <75:
        print("今天花溪",PM,"PM2.5")
        print("空气良好，适度户外运动！")
    elif PM>=75:
        print("今天花溪",PM,"PM2.5")
        print("空气污染，请小心")
    else:
        print("输入有误！")

#网站爬取
def crawl(url):
    try:
        #模拟浏览器
        headers = {
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36"
            }
        r = requests.get(url,timeout=30,headers=headers)
        r.raise_for_status()#如果状态码不是200，会引发HTTPerror异常
        r.encoding = r.apparent_encoding    #网站编码转换，避免错误编码
        
        #访问网站所返回的内容
        content = r.text

        #网站解析   （使用正则表达式）
        result = re.findall('div class="num">(.*)<',content)[0]
        return result
    except:
        print("产生异常")
        return 0

#数据保存
def save(PM):
    with open('save.txt','a+') as f:
        today = datetime.now()
        time = today.strftime("%Y-%m-%d %A")
        time = str(PM)+" "+time+'\n'
        if f.readlines(-1)!=time:
            f.write(time)
            print("保存数据成功")
        else:
            print("保存数据失败")
        f.close()


#程序入口点
if __name__ == '__main__':
    #http://tianqi.2345.com/air-60652.htm 该网站有问题PM2.5是动态展现的
    url='https://www.yangshitianqi.com/huaxi/kongqiwuran.html'

    #获取花溪PM的网页数据
    huaxi_PM = int(crawl(url))

    #数据保存
    save(huaxi_PM)

    #判断是否适宜出门
    pm(huaxi_PM)

'''

做题思路：
    1.找到目标网站
    2.利用requests urllib库爬取网站
        3.成功爬取网站后返回网页数据
        4.利用re（正则表达式）或者 Beautiful Soup 进行网页的数据的解析
        5.成功解析 并返回 想要的值
    6.利用 目标值 进行 功能实现

    '''

'''
题目要求：
    用python写网络爬虫花溪pm2.5的值并判断是否适宜出行
    



'''