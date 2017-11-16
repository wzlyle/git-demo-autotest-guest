# coding=utf-8

import unittest
import sys

sys.path.append("\source")
import source.my_sum


class MySum(unittest.TestCase):
    def setUp(self):  # 初始化
        pass

    # 测试用例，一定要以test开头
    def test_sum_001(self):
        self.assertEqual(source.my_sum.sum(1, 2), 3, 'test pass')

    def test_sum_002(self):
        self.assertEqual(source.my_sum.sum(1, 2), 3, 'test pass')

    def test_sub_001(self):
        self.assertEqual(source.my_sum.sub(4, 3), 1, 'test pass')

    def test_sub_002(self):
        self.assertEqual(source.my_sum.sub(10, 2), 8, 'test pass')

    def tearDown(self):  # 退出清理工作
        pass


if __name__ == "__main__":
    # unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(MySum("test_sum_001"))      # addTest()方法是向测试套件中添加测试用例
    suite.addTest(MySum("test_sum_002"))
    suite.addTest(MySum("test_sub_001"))
    suite.addTest(MySum("test_sub_002"))
    runner = unittest.TextTestRunner()
    runner.run(suite)

