from selenium import webdriver
import yaml,pymssql
# 设置浏览器对象
def setbrowser(BROWSER,URL):
    global browser
    if BROWSER=='Ie':
        browser=webdriver.Ie()
    elif BROWSER=='FireFox':
        browser=webdriver.Firefox()
    elif BROWSER=='Chrome':
        browser=webdriver.Chrome()
    browser.maximize_window()
    browser.implicitly_wait(5)
    browser.get(URL)
# 获取浏览器对象
def getbrowser():
    return browser
# 关闭浏览器
def closebrowser():
    browser.quit()
# 获取配置信息
def getdata(dir):
    with open(dir,'r',encoding='utf8') as file:
        Data=yaml.load(file,Loader=yaml.FullLoader)
    return Data
# 获取数据库连接
def setsql():
    global sql
    sql=pymssql.connect('192.168.100.233:1414','sa','000000','INTRUST')
# 获取数据库数据
def getsqldata(SQL):
    with sql.cursor() as cursor:
        cursor.execute(SQL)
        sqldata=list(cursor.fetchone())
    return sqldata
# 关闭数据库连接
def closesql():
    sql.close()
# 登录系统
def login():
    username=browser.find_element('id','username')
    username.clear()
    username.send_keys('admin')
    password=browser.find_element('id','password')
    password.clear()
    password.send_keys('000000')
    browser.find_element('tag name','button').click()
# 退出系统
def logout():
    browser.switch_to.default_content()
    browser.switch_to.frame('topFrame')
    browser.find_element('link text','退出系统').click()
    browser.switch_to.alert.accept()