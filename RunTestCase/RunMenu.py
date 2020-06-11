import sys,os
path = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(path)[0]
sys.path.append(rootPath)
from CreateTestCase.TestCaseScript import RunMenuTestCase

# 执行菜单用例，参数为菜单ID。
RunMenuTestCase.runmenutestcase('A0101')