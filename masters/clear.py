#清空爬虫工作状态，谨慎使用！
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
r.delete(queue_name)
r.delete(set_name)
r.delete(counter_name)

print("工作状态已清空！")

