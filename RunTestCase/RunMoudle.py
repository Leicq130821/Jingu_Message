import sys,os
path = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(path)[0]
sys.path.append(rootPath)
from CreateTestCase.TestCaseScript import RunMoudleTestCase

# 执行模块用例，参数为模块ID。
RunMoudleTestCase.runmoudletestcase()