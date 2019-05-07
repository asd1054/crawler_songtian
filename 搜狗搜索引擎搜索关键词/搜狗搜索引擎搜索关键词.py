##搜狗搜索引擎 https://www.sogou.com/web?query=外太空乌贼宇
#import requests
#kv = {'query':'外太空乌贼宇'}
#url = 'https://www.sogou.com/web'
##模拟浏览器
#headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36"
#    }
#r = requests.get(url,params = kv,timeout=30,headers=headers)
#r.raise_for_status()#如果状态码不是200，会引发HTTPerror异常
#r.encoding = r.apparent_encoding    #网站编码转换，避免错误编码
#len(r.text)

import requests
from bs4  import BeautifulSoup as bs
import bs4
import re
def getHtml(url,kv):
    try:
        headers = {
         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36"
        }
        r = requests.get(url,params = kv,timeout=30,headers=headers)
        r.raise_for_status()#如果状态码不是200，会引发HTTPerror异常
        r.encoding = r.apparent_encoding    #网站编码转换，避免错误编码
        return r.text
    except Exception as e:
        print("爬取失败！！！")
        print("错误信息：",e)
def parserHtml(html,ulist):
    soup = bs(html,"html.parser")
    contents  = soup.find('div',attrs = {'class':'results'})
    for content in contents.children:
        title = str(content.find('a'))
        title = re.findall('_blank">(.*?)</a>')[0]
        detail = content.find('p').contents
        details = str()
        for i in detail:
            details = str(i)
        ulist.append([title,detail])

def printList(ulist):
    for i in ulist:
        print(i[0],':')
        print(i[1],'\n')
    
def main():
    keyword = "外太空乌贼宇"
    url = 'https://www.sogou.com/web'
    kv = {'query':keyword}
    ulist = []
    html = getHtml(url,kv)
    parserHtml(html,ulist)
    printList(ulist)

main()

#360搜索引擎 http://www.so.com/s
#import requests
#from bs4  import BeautifulSoup as bs
#import bs4
#import re
#def getHtml(url,kv):
#    try:
#        headers = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36"
#        }
#        r = requests.get(url,params = kv,timeout=30,headers=headers)
#        r.raise_for_status()#如果状态码不是200，会引发HTTPerror异常
#        r.encoding = r.apparent_encoding    #网站编码转换，避免错误编码
#        return r.text
#    except Exception as e:
#        print("爬取失败！！！")
#        print("错误信息：",e)
#def parserHtml(html,ulist):
#    soup = bs(html,"html.parser")
#    contents  = soup.find('ul',attrs = {'class':'result'})
#    for content in contents.children:
#        title = str(content.find('a'))
#        title = re.findall('_blank">(.*?)</a>')[0]
#        detail = content.find('p').contents
#        details = str()
#        for i in detail:
#            details = str(i)
#        ulist.append([title,detail])

#def printList(ulist):
#    for i in ulist:
#        print(i[0],':')
#        print(i[1],'\n')
    
#def main():
#    keyword = "外太空乌贼宇"
#    url = 'http://www.so.com/s'
#    kv = {'q':keyword}
#    ulist = []
#    html = getHtml(url,kv)
#    parserHtml(html,ulist)
#    printList(ulist)

#main()

