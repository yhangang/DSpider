#默认的提取页面链接方法
from bs4 import BeautifulSoup

#page页面数据，tag需要提取的标签如'a'，attr需要提取的属性如'href'
def extract_urls(page, tag, attr):
    urls = set()
    data = BeautifulSoup(page, "html.parser")
     
    for x in data.findAll(tag):
        try:
            next_url = x[attr]
            urls.add(next_url)
        except:
            continue
         
    return urls