import threading
import configparser
from slaves.worker import run

#读取配置文件
cf = configparser.ConfigParser()
cf.read("../spider.conf","utf-8-sig")
slave_threads = cf.get("conf", "slave_threads")
slave_threads = int(slave_threads)


if slave_threads == None or slave_threads <= 0 or slave_threads > 10:
    print("线程数必须在1-10之间！")
    exit()
 
for i in range(slave_threads):
    t1 = threading.Thread(target=run,args=())
    t1.start()

