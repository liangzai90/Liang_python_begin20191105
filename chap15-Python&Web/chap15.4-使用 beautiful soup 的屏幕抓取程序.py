print("------ Beautiful Soup -------")
print("--------使用 beautiful soup 的屏幕抓取程序-------")

from urllib.request import urlopen
from bs4 import BeautifulSoup

text = urlopen('https://www.python.org/jobs').read()
soup = BeautifulSoup(text, 'html.parser')

jobs = set()
for job in soup.body.section('h2'):
    jobs.add('{}({})'.format(job.a.string, job.a['href']))

print('\n'.join(sorted(jobs, key=str.lower)))
