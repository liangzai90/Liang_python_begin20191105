print("----简单的 屏幕抓取 程序 ----")
from urllib.request import urlopen
import re

p = re.compile('<a href="(/jobs/\\d+)/">(.*?)</a>')
text = urlopen('https://www.python.org/jobs/').read().decode()
print("---------------------------start")
print(text)
print("---------------------------end")
for url, name in p.findall(text):
    print('{} ({})'.format(name, url))
