from selenium import webdriver

try:
    browser=webdriver.Ie()
    browser.maximize_window()
    browser.implicitly_wait(5)
    browser.get('http://192.168.100.233:7003')
    browser.find_element('id','username').send_keys('admin')
    password=browser.find_element('id','password')
    password.clear()
    password.send_keys('000000')
    browser.find_element('tag name','button').click()
    browser.switch_to.frame('topFrame')
    browser.find_element('id','mmenu8').click()
    browser.switch_to.default_content()
    browser.switch_to.frame('leftFrame')
    browser.switch_to.frame('leftiframe')
    browser.find_element('id','itemTextLink5').click()
    browser.find_element('id','itemTextLink9').click()
    browser.switch_to.default_content()
    browser.switch_to.frame('content')
    browser.find_element('name','btnNew').click()
    alert=browser.switch_to.alert
    alert.accept()
    alert=browser.switch_to.alert
    handles=browser.window_handles
    browser.switch_to.window(handles[-1])
    browser.find_element('name','btnSave').click()
except Exception as ERROR:
    print(ERROR)
finally:
    browser.quit()