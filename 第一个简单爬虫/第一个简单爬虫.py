
import requests
from bs4 import BeautifulSoup as bs

link = "http://www.santostang.com"
headers = {
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36"
            }
r = requests.get(link,headers = headers)#第一步：获取页面
soup = bs(r.text,'lxml')
title = soup.find("h1",class_ ="post-title").a.text.strip()#第二步：提取需要的数据

#数据保存
with open('title.txt','a+') as f:
    f.write(title+'\n')
    print("任务完成")
    f.close()
