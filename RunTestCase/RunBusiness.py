import sys,os
path = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(path)[0]
sys.path.append(rootPath)
from RunTestCase import RunBusinessTestCase

# 执行业务用例，参数为业务id。