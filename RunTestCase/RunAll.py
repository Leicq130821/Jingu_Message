import sys,os
path = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(path)[0]
sys.path.append(rootPath)
from CreateTestCase.TestCaseScript import RunAllTestCase

# 执行全部用例。
RunAllTestCase.runalltestcase()