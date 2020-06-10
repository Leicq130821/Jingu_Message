# 用于进入模块
from CreateTestCase.TestCaseScript import Global
import os

def entermoudle(moudle_id):
    # 获取CreateTestCase的路径
    current_path=os.path.dirname(os.path.dirname(__file__))
    # 获取浏览器对象
    browser= Global.getbrowser()
    # 获取进入模块的配置信息
    Data= Global.getdata(current_path + '/ConfigData/ENTERMOUDLE.yaml')[moudle_id]
    # 进入模块
    browser.switch_to.default_content()
    browser.switch_to.frame('topFrame')
    browser.find_element(Data[0],Data[1]).click()