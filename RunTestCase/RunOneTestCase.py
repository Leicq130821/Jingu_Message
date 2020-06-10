from CreateTestCase.TestCaseScript import Global,SendEmail
from HtmlTestRunnerNew import HTMLTestRunner
import unittest,os
from datetime import datetime

def runonetestcase(casename):
    # 建立数据库连接
    Global.setsql()
    # 获取项目根目录
    current_path = os.path.dirname(os.path.dirname(__file__))
    # 获取浏览器与地址数据
    browserdata = Global.getdata(current_path + r'/CreateTestCase/ConfigData/BROWSER_URL.yaml')
    for browser_url in browserdata:
        try:
            # 实例化浏览器并访问系统地址
            Global.setbrowser(browser_url[0],browser_url[1])
            # 登录系统
            Global.login()
            # 添加用例
            suite=unittest.defaultTestLoader.discover(current_path+r'/PageTestCase',pattern='%s.py'%casename)
            # 定义报告文件名及存放路径
            filename=current_path+r'\TestReport\OneTestCaseReport'+'\\%s'%browser_url[0]+'_%sReport_'%casename+datetime.now().strftime('%Y年%m月%d日_%H点%M分%S秒')+'.html'
            with open(filename,'wb') as file:
                runner=HTMLTestRunner(stream=file,title='%s执行%s'%(browser_url[0],casename))
                runner.run(suite)
            # 退出系统
            Global.logout()
        finally:
            # 关闭浏览器
            Global.closebrowser()
            # 发送邮件
            #SendEmail.sendemail(filename)
    # 断开数据库连接
    Global.closesql()