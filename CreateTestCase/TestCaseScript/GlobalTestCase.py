# 用于执行测试用例
from selenium.webdriver.support.select import Select
from CreateTestCase.TestCaseScript import Global

def globaltestcase(*DATA):
    # 获取浏览器对象
    browser = Global.getbrowser()
    # 取出SQL语句
    DATA=list(DATA)
    SQL=DATA.pop()
    # 用于存放输入的值
    INPUTDATA=[]
    RESULT=1
    TEXT=''
    SQLDATA=[]
    JSERROR=0
    # 执行用例
    try:
        for data in DATA:
            if JSERROR==1:
                break
            # 1.元素输入值：[1,定位元素的方法,定位元素所需参数,输入的值]
            if data[0]==1:
                element=browser.find_element(data[1],data[2])
                element.clear()
                element.send_keys(data[3])
                INPUTDATA.append(data[3])
            # 2.点击：[2,定位元素的方法,定位元素所需参数]
            elif data[0]==2:
                element=browser.find_element(data[1],data[2])
                element.click()
            # 3.下拉选项操作：[3,定位元素的方法,定位元素所需参数,下拉选项的VALUE]
            elif data[0]==3:
                Select(browser.find_element(data[1],data[2])).select_by_value(data[3])
                INPUTDATA.append(data[3])
            # 4.切换frame/iframe表单：[4,frame/iframe的属性值]
            elif data[0]==4:
                browser.switch_to.frame([data[1]])
            # 5.切换默认表单：[5]
            elif data[0] == 5:
                browser.switch_to.default_content()
            # 6.切换窗口：[6,切换窗口的索引]
            elif data[0]==6:
                handles=browser.window_handles
                if data[1]==0:
                    if len(handles)>1:
                        RESULT=2
                        alert=browser.switch_to.alert
                        TEXT=alert.text
                        alert.accept()
                        browser.close()
                        JSERROR=1
                    browser.switch_to.window(handles[data[1]])
                elif data[1]==-1:
                    browser.switch_to.window(handles[data[1]])
            # 7.接受弹出框：[7]
            elif data[0]==7:
                alert=browser.switch_to.alert
                TEXT=alert.text
                if '成功' not in TEXT:
                    RESULT = 2
                else:
                    RESULT = 1
                alert.accept()
            # 8.弹出框输入值：[8,输入的值]
            elif data[0]==8:
                browser.switch_to_alert().send_keys(data[1])
            # 9.执行JS语句：[9,JS语句]
            elif data[0]==9:
                browser.execute_script(data[1])
    except Exception as ERROR:
        RESULT = 3
        TEXT=ERROR
        handles=browser.window_handles
        if len(handles)>1:
            browser.close()
            browser.switch_to.window(handles[0])
    # 获取数据库的结果数据
    if RESULT==1:
        SQLDATA = Global.getsqldata(SQL)
    return INPUTDATA,SQLDATA,RESULT,TEXT