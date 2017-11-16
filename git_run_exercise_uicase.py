#coding=utf-8

import unittest
import os
import sys
import time
import HTMLTestRunner
reload(sys)
sys.setdefaultencoding('utf8')

def gen_test_suite():
    testunit = unittest.TestSuite()
    test_dir = os.path.abspath(os.path.dirname(__file__)) + os.sep + 'testcase\exercise_uicase'
    print "The path to the testcase is:",test_dir

    discover = unittest.defaultTestLoader.discover(test_dir,pattern='case_*.py',top_level_dir=None)
    for test_suite in discover:
        for test_case in test_suite:
            testunit.addTest(test_case)
            print testunit
    return testunit

if __name__ == '__main__':
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    filename = "F:\\Demo\\Demo_Git\\git-demo-autotest-guest\\report\\" + now + '_Exercise_UI_AutoTest_Report.html'
    fp = file(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title=u'UI层自动化测试报告',
        description=u'测试用例执行情况：',
    )
    all_test_units = gen_test_suite()
    runner.run(all_test_units)
    fp.close()