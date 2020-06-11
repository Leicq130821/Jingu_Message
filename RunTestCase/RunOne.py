import sys,os
path = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(path)[0]
sys.path.append(rootPath)
from CreateTestCase.TestCaseScript import RunOneTestCase

# 具体执行某个用例，参数为文件名。
RunOneTestCase.runonetestcase('MODI集团信息')