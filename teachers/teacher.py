import unittest
import os
from HTMLTestRunner import HTMLTestRunner
suite=unittest.TestSuite()
tests=unittest.defaultTestLoader.discover(os.getcwd(),"test.py")
suite.addTest(tests)
#使用html运行器，生成以html结果报告
f = open("讲师评价系统测试报告.html","w+",encoding="utf-8")
runner = HTMLTestRunner.HTMLTestRunner(
    stream = f,
    verbosity = 1,
    title = "讲师评价系统的测试报告"
)
#使用运行器来运行测试集
runner.run(suite)