#coding:utf-8
# from selenium import webdriver
# from time import sleep
#
# chrome_driver = r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
# #chrome_driver = r"D:\Python27\Lib\site-packages\selenium\webdriver\chrome\chromedriver.exe"
# browser = webdriver.Chrome(executable_path=chrome_driver)
# browser.get("http://passport.roobo.net/#/login")
# sleep(2)
# elem=browser.find_element_by_css_selector("#app > div > div.box-flex-6 > div > div.login-box > form > div:nth-child(1) > div > div.el-input > input")
# elem.send_keys("maxiaoli@roobo.com")
# elem=browser.find_element_by_css_selector("#app > div > div.box-flex-6 > div > div.login-box > form > div:nth-child(2) > div > div.el-input > input")
# elem.send_keys("123456")
# elem=browser.find_element_by_css_selector("#app > div > div.box-flex-6 > div > div.login-box > form > div:nth-child(3) > div > button")
# elem.click()

# sleep(10)
# #退出
# browser.close()
# browser.quit()

# # print(browser.page_source)
from openBrowser   import openBrowser
#
if __name__ == "__main__":
    openbrowser = openBrowser('http://passport.roobo.net/#/login',"maxiaoli@roobo.com","123456")
    openbrowser.login()