import configparser
import redis
import requests
import time
from slaves import handler
from slaves import extracter

#读取配置文件
cf = configparser.ConfigParser()
cf.read("../spider.conf","utf-8-sig")
redis_host = cf.get("redis", "redis_host")
redis_port = cf.get("redis", "redis_port")
redis_auth = cf.get("redis", "redis_auth")
 
queue_name = cf.get("conf", "queue_name")
set_name = cf.get("conf", "set_name")
counter_name = cf.get("conf", "counter_name")
init_page = cf.get("conf", "init_page")

#slave初始化工作
r = redis.StrictRedis(host=redis_host, port=redis_port) 
file_path = "E:/pic/1/"
s = requests.session()
i = 0;


#开始爬取网页
while True:
    url = r.lpop(queue_name)
    if url == None:
        time.sleep(3)
        continue
    url = url.decode("UTF-8")
    count = r.get(counter_name).decode('UTF-8')
    print('已经抓取：' + count + '个，正在抓取-->' + url)
    r.incr(counter_name)
    
    #下载网页准备处理
    try:
        page = s.get(url, timeout = 2)
        page.encoding = 'UTF-8'
    except:
        continue
    
    urls = extracter.extract_urls(page.text, 'a', 'href')
    for x in urls:
        if 'mm.taobao.com' in x:
            if r.sadd(set_name,"https:" + x) == 1:
                r.rpush(queue_name,"https:" + x)
                
    links = extracter.extract_urls(page.text, 'img', 'src')
    for x in links:
        print("正在保存图片" + str(i) + "-->https:" + x)
        try:
            handler.save_file_binary(file_path +str(i) +".jpg", s.get("https:" + x, timeout = 2).content)
            i += 1
        except:
            continue
            
    