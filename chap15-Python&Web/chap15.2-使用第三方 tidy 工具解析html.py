print("------ 使用第三方 tidy 工具解析html-----")

from subprocess import Popen, PIPE
text = open("messy.html").read()

# http://www.html-tidy.org/ 下载 tidy.exe
# 去https://github.com/htacg/tidy-html5/releases/tag/5.6.0 官网下载 tidy.exe文件，放在当前目录
tidy = Popen('tidy', stdin=PIPE, stdout=PIPE, stderr=PIPE)

tidy.stdin.write(text.encode())
tidy.stdin.close()

print(tidy.stdout.read().decode)
