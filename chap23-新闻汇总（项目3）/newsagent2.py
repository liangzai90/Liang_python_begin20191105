# -*- coding: utf-8 -*-

from nntplib import NNTP, decode_header
from urllib.request import urlopen
import textwrap
import re

class NewsAgent:
    """
    可将新闻源中的新闻分发到新闻目的地对象
    """
    def __init__(self):
        self.sources = []
        self.destinations = []
    def add_source(self, source):
        self.sources.append(source)
    def addDestination(self, dest):
        self.destinations.append(dest)
    def distribute(self):
        """
        从所有新闻源获取所有的新闻，并将其分发到所有新闻目的地
        :return:
        """
        items = []
        for source in self.sources:
            items.extend(source.get_items())
        for dest in self.destinations:
            dest.receive_items(items)

class NewsItem:
    """
    由标题和正文组成的简单新闻
    """
    def __init__(self, title, body):
        self.title = title
        self.body = body

class NNTPSource:
    """
    从NNTP新闻组获取新闻的新闻源
    """
    def __init__(self, servername, group, howmany):
        self.servername = servername
        self.group = group
        self.howmany = howmany
    def get_items(self):
        server = NNTP(self.servername)
        resp, count, first, last, name = server.group(self.group)
        start = last - self.howmany + 1
        resp, overviews = server.over((start, last))
        for id, over in overviews:
            title = decode_header(over['subject'])
            resp, info = server.body(id)
            body = '\n'.join(line.decode('latin') for line in info.lines) + '\n\n'
            yield NewsItem(title, body)
        server.quit()

class SimpleWebSource:
    """
    使用正则表达式从网页提取新闻的新闻源
    """
    def __init__(self, url, title_pattern, body_pattern, encoding='utf-8'):
        self.url = url
        self.title_pattern = re.compile(title_pattern)
        self.body_pattern = re.compile(body_pattern)
        self.encoding = encoding
    def get_items(self):
        text = urlopen(self.url).read().decode(self.encoding)
        titles = self.title_pattern.findall(text)
        bodies = self.body_pattern.findall(text)
        for title, body in zip(titles, bodies):
            yield NewsItem(title, textwrap.fill(body) + '\n')

class PlainDestination:
    """
    以纯文本方式显示所有新闻的新闻目的地
    """
    def receive_items(self, items):
        for item in items:
            print(item.title)
            print('-' * len(item.title))
            print(item.body)

class HTMLDestination:
    """
    以HTML格式显示所有新闻的新闻目的地
    """
    def __init__(self, filename):
        self.filename = filename
    def receive_items(self, items):
        out = open(self.filename, 'w')
        print("""
        <html>
          <head>
            <title>Today's News</title>
          </head>
          <body>
          <h1>Today's News</h1>
        """, file=out)
        print('<ul>', file=out)
        id = 0
        for item in items:
            id += 1
            print('<li><a href="#{}">{}</a></li>'.format(id, item.title), file=out)
        print('</ul>', file=out)

        id = 0
        for item in items:
            id += 1
            print('<h2><a name="{}">{}</a></h2>'.format(id, item.title), file=out)
            print('<pre>{}</pre>'.format(item.body), file=out)
        print("""
        </body>
        </html>
        """, file=out)

def runDefaultSetup():
    """
    默认的新闻源和目的地设置，请跟进偏好进行修改
    :return:
    """
    agent = NewsAgent()
    reuters_url = 'https://www.python.org/'
    reuters_title = r'<h2><a href="[^"]*"\s*>(.*?)</a>'
    reuters_body = r'</h2><p>(.*?)</p>'
    reuters = SimpleWebSource(reuters_url, reuters_title, reuters_body)
    agent.add_source(reuters)

    clpa_server ='news.gmane.org'
    clpa_group = 'gmane.comp.python.committers'
    clpa_howmany = 2
    clpa = NNTPSource(clpa_server, clpa_group, clpa_howmany)
    agent.add_source(clpa)

    # 添加纯文本目的地和HTML目的地
    agent.addDestination(PlainDestination())
    agent.addDestination(HTMLDestination('news.html'))

    # 分发新闻
    agent.distribute()

if __name__ == '__main__':
    runDefaultSetup()
