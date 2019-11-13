# -*- coding: utf-8 -*-
print("-----使用模块 subprocess 调用外部检查器----")

import unittest, my_math2
from subprocess import Popen, PIPE
class ProductTestCase(unittest.TestCase):
    def test_with_PyLint(self):
        cmd = 'pylint', '-rn', 'my_math2'
        pylint = Popen(cmd, stdout=PIPE, stderr=PIPE)
        print("----------------------------start")
        print(pylint.stdout.read().decode())
        print("----------------------------End")
        self.assertEqual(pylint.stdout.read(), b'', '这里是在做啥检查啊！')

if __name__ == '__main__': unittest.main()

