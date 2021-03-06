from CreateTestCase.TestCaseScript import Global,GlobalTestCase,EnterMenu
import unittest,os

class ModiJTXX(unittest.TestCase):
    def testModiJTXX(self):
        # 路径信息
        current_path = os.path.dirname(__file__)
        datafilename = os.path.basename(__file__)[:-3]
        # 根据路径获取菜单的ID
        menu_id=current_path.split('\\')[-1][:5]
        # 进入菜单
        EnterMenu.entermenu(menu_id)
        # 获取用例信息
        Data= Global.getdata(current_path+'/%s.yaml'%datafilename)
        # 执行用例并获取输入与输出值
        INPUTDATA,SQLDATA,RESULT,TEXT=GlobalTestCase.globaltestcase(*Data)
        if RESULT==1:
            print(TEXT)
            print('输入数据：',INPUTDATA)
            print('结果数据：',SQLDATA)
            assert INPUTDATA==SQLDATA,'输入的值与存入到数据库的值不一致，请检查!'
        elif RESULT == 2:
            assert False, '页面报错，请检查！：\n%s' % TEXT
        elif RESULT == 3:
            assert False, '执行报错，请检查！：\n%s' % TEXT