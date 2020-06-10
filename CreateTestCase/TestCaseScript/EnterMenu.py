from CreateTestCase.TestCaseScript import Global,EnterMoudle
import os

def entermenu(menu_id):
    # 获取CreateTestCase的路径
    current_path=os.path.dirname(os.path.dirname(__file__))
    # 获取浏览器对象
    browser= Global.getbrowser()
    # 进入模块
    moudle_id=menu_id[:1]
    EnterMoudle.entermoudle(moudle_id)
    # 进入菜单所在表单
    browser.switch_to.default_content()
    browser.switch_to.frame('leftFrame')
    browser.switch_to.frame('leftiframe')
    # 获取菜单配置信息
    Data= Global.getdata(current_path + '/ConfigData/ENTERMENU.yaml')[menu_id[:1]]
    # 取出进入菜单的方法
    list=[]
    while menu_id in Data:
        list.insert(0,Data[menu_id])
        menu_id=menu_id[:-2]
    # 进入菜单
    for data in list:
        browser.find_element(data[0],data[1]).click()
    # 进入操作的表单页面
    browser.switch_to.default_content()
    browser.switch_to.frame('content')