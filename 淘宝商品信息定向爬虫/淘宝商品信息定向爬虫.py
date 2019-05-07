
#为确保您账户的安全及正常使用，依《网络安全法》相关要求，6月1日起会员账户需绑定手机。如您还未绑定，请尽快完成，感谢您的理解及支持！ 
#需要登陆才能使用。。。。。。。。。。。

import re
import requests

def getHtml(url):
    try:
        header = {

            "cookie": "t=e7d9f4c7f3227f915fbd48e7e26224b0; cna=oG3+E4sxa0gCAXW8fBjp9brg; hng=CN%7Czh-CN%7CCNY%7C156; thw=cn; miid=944979071213674707; UM_distinctid=165ae188c3c0-0c0f7333a6eeec-514d2f1f-1fa400-165ae188c3d2cc; tracknick=%5Cu4E94%5Cu7EA7%5Cu82B1; tg=0; tk_trace=oTRxOWSBNwn9dPyorMJE%2FoPdY8zZPEr%2FCrvCMS%2BG3sTRRWrQ%2BVVTl09ME1KrXkVhSSwUFB92f7HO4iiBoqEIJPLTyFa5TWm%2F8qBT26fbUSYtQ5PCsw5KRV4VCHxmGQHD5XLkFr3qSnEW8ZYAa9lG%2F27DGssJqlYMsaREyY4ozp6Rs6dIh4%2BaPwKgVy9%2Bys%2Fw%2FfFtwLFs8uMqZKcc97KMoqDVwaq5DPfVErFw1yJS4MaTWztoDrA9fIJy4Sai52CGfIEUnqF4PVtnmnUb7ZKj9PElYzOdipq1lr7fyEL1vyihytqNtKZ8%2BWmbZ3fmGOy4ANGR7q95t1rlWgA18A%3D%3D; v=0; cookie2=19ac5feae34fa615665f7fad259bb227; _tb_token_=3eebf30e3db77; unb=2168414704; sg=%E8%8A%B14c; _l_g_=Ug%3D%3D; skt=1ffe287af1fc209a; cookie1=B0eg4Ua28r7hNKsL1js8dtvwaRXzehEUkzuohumUNaI%3D; csg=200cdc47; uc3=vt3=F8dByR%2FOenHy50ShG7M%3D&id2=UUkIHSKbdvpH5A%3D%3D&nk2=rXwG9YZO&lg2=UIHiLt3xD8xYTw%3D%3D; existShop=MTU0MTkwNTY5Mg%3D%3D; lgc=%5Cu4E94%5Cu7EA7%5Cu82B1; _cc_=UtASsssmfA%3D%3D; dnk=%5Cu4E94%5Cu7EA7%5Cu82B1; _nk_=%5Cu4E94%5Cu7EA7%5Cu82B1; cookie17=UUkIHSKbdvpH5A%3D%3D; enc=Qj3JsjIBKf%2FROj%2FWEjn%2FcwF537eJMrJTRh7r3rZHT68whP%2BUW%2FFGxHeR1FjGTi1ETinnfIMlrB51vH6wKYkcHA%3D%3D; alitrackid=www.taobao.com; lastalitrackid=www.taobao.com; SL_GWPT_Show_Hide_tmp=1; SL_wptGlobTipTmp=1; swfstore=59664; x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0%26__ll%3D-1%26_ato%3D0; Hm_lvt_cdce8cda34e84469b1c8015204129522=1541905764,1541908477; _m_h5_tk=69b0875849756d94f1c70cebb7c2068f_1541916823970; _m_h5_tk_enc=4b669232523f217e64a101ef6f9c2cc2; mt=ci=-1_1; uc1=cookie16=VFC%2FuZ9az08KUQ56dCrZDlbNdA%3D%3D&cookie21=UtASsssmfaCONGki79doeA%3D%3D&cookie15=UtASsssmOIJ0bQ%3D%3D&existShop=false&pas=0&cookie14=UoTYN4iDacOqOg%3D%3D&cart_m=0&tag=8&lng=zh_CN; whl=-1%260%261541908467273%261541941334138; JSESSIONID=51E575D699AB4354AD345A2C741EC2E0; Hm_lpvt_cdce8cda34e84469b1c8015204129522=1542256091; isg=BJeXv-9LgALAPQQb9rL24IPWJgshdGpagKvl1unF02bAGLda8azPjqs6fvij8EO2",

            "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36",

            "referer": "https://s.taobao.com/search?q="
            
            }

        r= requests.get(url,timeout =30,headers=header)
        r.raise_for_status()
        r.enconding = r.apparent_encoding
        return r.text
    except:
        return ''

def parsePage(ilt,html):
    try:
        plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"',html)
        tlt = re.findall(r'\"raw_title\"\:\".*?"',html)
        for i in range(len(plt)):
            price = eval(plt[i].split(':')[1])
            title = eval(tlt[i].split(':')[1])
            ilt.append([price,title])
    except Exception as e:
        print(e)

def printGoods(ilt):
    tplt = "{:4}\t{:8}\t{:16}"
    print(tplt.format("序号","价格","商品名称"))
    count = 0
    for g in ilt:
        count = count +1
        print(tplt.format(count,g[0],g[1]))

def main():
    goods  =  input("请输入要搜索的信息:")
    #goods = '鼠标'
    depth =2 
    start_url = 'https://s.taobao.com/search?q='+goods
    infoList = []

    for i in range(depth):
        try:
            url = start_url +'&s=='+str(44*i)
            html = getHtml(url)
            parsePage(infoList,html)
        except Exception as e:
            print(e)
            continue

    #对价格进行排序
    infoList = sorted(infoList,key = lambda s :s[0])
    printGoods(infoList)

main()

