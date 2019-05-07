import requests
from  multiprocessing import Pool
#y原理就是直接去VIP解析网站下载零碎的解析视频，然后拼接在一起

#第一步先把每一个片段给下载下来
def temp(i):
    try:
        url = "http://v22.51cto.com/2017/12/11/207794/5761/high/loco_video_516000_%d.ts"%(i)

        #模拟浏览器
        headers = {
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36"
            }
        r = requests.get(url,headers=headers)
        #现在有了r.content 这个视频的二进制数据，我们就可以直接来保存视频了
        f = open('./1/{}'.format(url[-10:]),'ab')
        f.write(r.content)
        print(i)
        f.close()
    except:
        print("第",i,"条出错了")

if __name__=='__main__':
    pool=Pool(20)
    for i in range(1000):
        pool.apply_async(temp,(i,))
    pool.close()
    pool.join()
    

    
