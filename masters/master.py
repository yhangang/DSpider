import configparser
import redis

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

#初始化爬虫状态
r = redis.StrictRedis(host=redis_host, port=redis_port) 
#sadd成功插入返回1，失败返回0
if r.sadd(set_name,init_page) == 1:
    r.rpush(queue_name,init_page)
    print("爬虫初始化完毕！")
else:
    print("初始化失败，该链接已经过处理！")