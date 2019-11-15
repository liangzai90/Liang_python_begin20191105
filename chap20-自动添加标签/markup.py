# -*- coding: utf-8  -*-
import logging
import sys, re
from handlers import *
from util import *
from rules import *

logging.basicConfig(level=logging.INFO, filename="mylog.log")

class Parser:
    """
    Parser读取文本文件，应用规则并控制处理程序
    """
    def __init__(self, handler):
        self.handler = handler
        self.rules = []
        self.filters = []
    def addRule(self, rule):
        self.rules.append(rule)
    def addFilter(self, pattern, name):
        def filter(block, handler):
            return re.sub(pattern, handler.sub(name), block)
        self.filters.append(filter)

    def parse(self, file):
        self.handler.start('document')
        logging.info("--------------CC")
        for block in blocks(file):
            logging.info("--------------DD")
            logging.info(block)

            for filter in self.filters:
                logging.info("--------------EE")
                logging.info(filter)

                block2 = filter(block, self.handler)
                for rule in self.rules:
                    logging.info("--------------FF")
                    logging.info(block2)

                    if rule.condition(block2):
                        logging.info("--------------GG")
                        logging.info(block2)

                        last = rule.action(block2, self.handler)
                        if last: break
        self.handler.end('document')

class BasicTextParser(Parser):
    """
    在构造函数中添加规则和过滤器的Parser子类
    """
    def __init__(self, handler):
        Parser.__init__(self, handler)
        self.addRule(ListRule())
        self.addRule(ListItemRule())
        self.addRule(TitleRule())
        self.addRule(HeadingRule())
        self.addRule(ParagraphRule())

        self.addFilter(r'\*(.+?)\*', 'emphasis')
        self.addFilter(r'(http://[\.a-zA-Z/]+)', 'url')
        self.addFilter(r'([\.a-zA-Z]+@[\.a-zA-Z]+[a-zA-Z]+)', 'mail')

handler = HTMLRenderer()
parser = BasicTextParser(handler)
# 打印日志，查找问题。目前来看stdin的字符串是没有问题的
# logging.info(sys.stdin.read())

parser.parse(sys.stdin)

# 在 Cygwin下面执行这个 Linux 命令
# python markup.py  < test_input.txt > output.html
