
"""

爬虫框架结构： 5 + 2 结构
    
    1.Engine    不需要用户修改
        1.控制所有模块之间的数据流
        2.根据条件触发事件

    2.Downloader    不需要用户修改
        根据请求下载网页

    3.Scheduler 不需要用户修改
        对所有爬取请求进行调度管理

    4.Spider    需要用户编写配置代码
        1.解析Downloader返回的响应（Response）
        2.产生爬取项（scraped item）
        3.产生额外的爬取请求（Request）

    5.Item Pipelines    需要用户编写配置代码
        1.以流水线方式处理Spider产生的爬取项
        2.由一组操作顺序组成，类似流水线，每个操作是一个Item Pipeline类型
        3.可能操作包括：请理、检验和查重爬取项中的HTML数据、将数据存储到数据库


    Downloader Middleware
        目的：
            实施Engine、Scheduler和Downloader之间进行用户可配置的控制
        功能：
            修改、丢弃、新增请求或响应


"""


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

"""
命令行格式使用scrapy 框架    

    startprojest    创建一个新工程     
    genspider       创建一个爬虫
    settings        获得爬虫配置信息
    crawl           运行一个爬虫
    list            列出工程中所有爬虫
    shell           启动URL调试命令行


"""


"""
    yield（生成器） 的优势
        更节省存储空间
        响应更迅速
        使用更灵活

def gen(n):
    for i in range(n):
        yield i**2

两者等价

def gen(n):
    ls = [i**2 for i in range(n):]
    return ls

"""

"""
    scrapy爬虫的使用步骤
        步骤1.创建一个工程和Spider模板
        步骤2.编写Spider
        步骤3.编写Item Pipeline
        步骤4.优化配置策略

    scrapy爬虫的数据类型
        Requests类       
                表示一个http请求
                由Spider生成，由Downloader执行
                    .url        Request对应的请求URL地址
                    .method     对应的请求方法，‘GET’，‘POST’等
                    .headers    字典类型风格的请求头
                    .body       请求内容主体，字符串类型
                    .meta       用户添加的拓展信息，在scrapy内部模块间传递信息使用
                    .copy()     复制该请求
        Response类
                表示一个http响应
                由Downloader生成，由Spider处理
                    .url        Response对应的URL地址
                    .status     HTTP状态码， 默认是200
                    .headers    Response对应的头部信息
                    .body       Response对应的内容信息，字符串类型
                    .flag       一组标记
                    .request    产生Response类型对应的Request对象
                    .copy()     复制该响应
        Item类
                表示一个从HTML页面中提取的信息内容
                由Spider生成，由Item Pipeline处理

"""