#coding=utf-8

import unittest
import sys

# 把source目录添加到path下，这里用相对路径
sys.path.append("\source")

from source import my_hello

class MyHello(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_hello(self):
        my_hello.hello("baidu.com")

if __name__ == "__main__":
    unittest.main()
