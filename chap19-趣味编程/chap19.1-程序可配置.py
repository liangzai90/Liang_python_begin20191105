#让程序可配置

# 方法1：
# 专门为配置创建一个模块，然后 import 这个模块来实现程序的可配置

# 方法2：使用标准库模块（configparser）
print("----一个使用ConfigParser的程序------")

from configparser import ConfigParser

CONFIGFILE = "area.ini"

config = ConfigParser()

# 读取配置文件
config.read(CONFIGFILE)

# 打印默认问候语(greeting)
# 在 messages 部分查找问候语
print(config['messages'].get('greeting'))

# 使用配置文件中的提示（questing）让用户输入半径
radius = float(input(config['messages'].get('question')) + ' ')

# 打印配置文件中的结果消息(result_message)
# 以空格结束以便接着在当前行打印
print(config['messages'].get('result_message'), end=" ")

# getfloat() 将获取的值转换为浮点数
print(config['numbers'].getfloat('pi') * radius ** 2)
