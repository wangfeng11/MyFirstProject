#!/usr/bin/env python
# -*- conding:utf-8 -*-
# author:wangfeng
import os.path
import unittest
from HTMLTestRunner_PY3 import *
import os, sys


class demo(unittest.TestCase):
    # 类就要加该修饰符
    @classmethod
    def setUpClass(cls) -> None:
        print("setup class")

    @classmethod
    def tearDownClass(cls) -> None:
        print("tearDown class")

    def setUp(self) -> None:
        print("setup")

    def tearDown(self) -> None:
        print("teardown")
        print("")

    def test_case01(self):
        print("testcase01")
        self.assertEqual(1, 1, '判断相等')
        self.assertIn('h', 'this', '不在里面')

    def test_case02(self):
        print("testcase02")
        self.assertEqual(2, 3, '判断相等')
        self.assertIn('h', 'this', '不在里面')

    @unittest.skipIf(1 + 1 == 2, "跳过这条用例")
    def test_case03(self):
        print("testcase03")
        self.assertEqual(3, 3, '判断相等')
        self.assertIn('h', 'this', '不在里面')


class demo1(unittest.TestCase):
    def test_demo1_case0(self):
        print("test_demo1_case0")

    def test_demo1_case1(self):
        print("test_demo1_case1")


class demo2(unittest.TestCase):
    def test_demo2_case0(self):
        print("test_demo2_case0")

    def test_demo2_case1(self):
        print("test_demo2_case1")


if __name__ == '__main__':
    # 执行方法一：
    # unittest.main()

    # 执行方法二,以测试用例为单位，可执行指定用例：
    # suit = unittest.TestSuite()
    # suit.addTest(demo("test_case01"))
    # suit.addTest(demo1("test_demo1_case0"))
    # unittest.TextTestRunner().run((suit))

    # 执行方法三，以类为单位，可执行指定类：
    # suite1 = unittest.TestLoader().loadTestsFromTestCase(demo)
    # suite2 = unittest.TestLoader().loadTestsFromTestCase(demo1)
    # suiteAll = unittest.TestSuite([suite1, suite2])
    # unittest.TextTestRunner().run(suiteAll)

    # 执行方法四，
    discover = unittest.defaultTestLoader.discover("./", pattern="test*.py")
    # unittest.TextTestRunner().run(discover)

    # 测试报告
    # 对于模块和自己写的脚本不在同一个目录下，在脚本开头加sys.path.append('引用模块的地址')：
    sys.path.append('D:/Work/Pycharm-workspace/MyFirstProject/test_unittest')
    # 设置报告路径
    report_path = os.path.join(os.path.dirname(__file__), 'report')
    # 通过当前时间命名报告
    now = time.strftime("%Y-%m-%d %H_%M_%S", time.localtime())
    report_name = report_path + "/" + now + "_result.html"
    report_title = 'Example用例执行报告'
    desc = '用于展示HTMLTestRunner'
    # report_file = './ExampleReport.html'
    with open(report_name, 'wb') as report:
        runner = HTMLTestRunner(stream=report, title=report_title, description=desc)
        runner.run(discover)
