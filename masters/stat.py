#输出爬虫当前状态
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

#输出当前工作状态
r = redis.StrictRedis(host=redis_host, port=redis_port) 
visited = r.get(counter_name)
if visited == None:
    visited = 0
else:
    visited = visited.decode('UTF-8')
to_be_visit = r.llen(queue_name)
set_len = r.scard(set_name)

print("已经爬取网页个数：" + str(visited))
print("待爬队列长度：" + str(to_be_visit))
print("过滤器元素个数：" + str(set_len))

