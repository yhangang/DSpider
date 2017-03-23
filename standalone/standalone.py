from collections import deque
import re
import urllib.request
from tools import tool
import arrow

#存储爬到的网页
def saveToFile(filePath,data):
    with open(filePath,'w',encoding='utf-8') as fileop:
        fileop.write(data)

queue = deque()
visited = set()

init_url = "http://www.badtom.cn"

queue.append(init_url)
visited.add(init_url)
#通过头信息伪装成火狐浏览器
headinfo = {
    'Connection': 'Keep-Alive',
    'Accept': 'text/html, application/xhtml+xml, */*',
    'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'
}

filePath = 'C:/d/spider/standalone/'
count = 0
start_time = arrow.now().timestamp

while queue:
    url = queue.popleft()
    print('已经抓取：' + str(count) + '个，正在抓取-->' + url)
    count += 1
    fname = tool.url_replace(url)

    try:
        req = urllib.request.Request(url,headers = headinfo)
        urlop = urllib.request.urlopen(req,timeout = 2)
        data = urlop.read().decode('utf-8')
        saveToFile(filePath + fname + '.html', data)
    except:
        continue

    linkre = re.compile('href="(.+?)"')
    linkdata = linkre.findall(data)
    for next_url in linkdata:
        if 'http' in next_url and 'badtom.cn' in next_url and next_url not in visited:
            queue.append(next_url)
            visited.add(next_url)
            
end_time = arrow.now().timestamp
print("爬取" + str(count) + "个网页，花费" + str(end_time - start_time) + "秒")