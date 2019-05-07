'''
步骤1 ：
    从网上获取大学排名网页内容
    getHTMLText（）
步骤2 ：
    提取网页内容中信息到合适的数据结构
    fillUnivList（）
步骤3 ：
    利用数据结构展示并输出结果
    printUnivList（）

'''
#coding = "utf-8"
import bs4
from bs4 import BeautifulSoup as bs
import requests
#获取网页信息
def getHTMLText(url):   
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        content = r.text
        return content
    except:
        print("获取网页失败")
        return ''
#将网页中需要的信息提取出来  列表形式 【名词，大学名称，省市，总分】
def fillUnivList(ulist,html):
    soup = bs(html,"html.parser")
    with open('大学排名.csv','a+') as f:
        for tr in soup.find('tbody').children:
            if isinstance(tr,bs4.element.Tag):
                tds = tr('td')
                ulist.append([tds[0].string,tds[1].string,tds[2].string,tds[3].string])
                f.write("{},{},{},{},{}\n".format(tds[0].string,tds[1].string,tds[2].string,tds[3].string))
#打印大学信息
def printUnivList(ulist,num):
    print("{:^10}\t{:^20}\t{:^10}{:^10}".format("排名","学校名称","省市","总分"))
    for i in range (num):
        u = ulist[i]
        print("{:^10}\t{:^20}\t{:^10}{:^10}".format(u[0],u[1],u[2],u[3]))

def main ():
    uinfo = []
    url = 'http://www.zuihaodaxue.com/zuihaodaxuepaiming2018.html'
    html  = getHTMLText(url)
    fillUnivList(uinfo,html)
    printUnivList(uinfo,20)

main()


##CrawUnivRankingB.py
#import requests
#from bs4 import BeautifulSoup
#import bs4
 
#def getHTMLText(url):
#    try:
#        r = requests.get(url, timeout=30)
#        r.raise_for_status()
#        r.encoding = r.apparent_encoding
#        return r.text
#    except:
#        return ""
 
#def fillUnivList(ulist, html):
#    soup = BeautifulSoup(html, "html.parser")
#    for tr in soup.find('tbody').children:
#        if isinstance(tr, bs4.element.Tag):
#            tds = tr('td')
#            ulist.append([tds[0].string, tds[1].string, tds[3].string])
 
#def printUnivList(ulist, num):
#    tplt = "{0:^10}\t{1:{3}^10}\t{2:^10}"
#    print(tplt.format("排名","学校名称","总分",chr(12288)))
#    for i in range(num):
#        u=ulist[i]
#        print(tplt.format(u[0],u[1],u[2],chr(12288)))
     
#def main():
#    uinfo = []
#    url = 'http://www.zuihaodaxue.cn/zuihaodaxuepaiming2018.html'
#    html = getHTMLText(url)
#    fillUnivList(uinfo, html)
#    printUnivList(uinfo, 20) # 20 univs
#main()