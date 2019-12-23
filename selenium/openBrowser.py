#coding:utf-8

from selenium import webdriver
from time import sleep

class openBrowser(object):
    def __init__(self,url,user,password):
        self.url=url
        self.user=user
        self.password=password
    def login(self):
        chrome_driver = r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
        # chrome_driver = r"D:\Python27\Lib\site-packages\selenium\webdriver\chrome\chromedriver.exe"
        browser = webdriver.Chrome(executable_path=chrome_driver)
        browser.get(self.url)
        sleep(2)
        elem = browser.find_element_by_css_selector(
            "#app > div > div.box-flex-6 > div > div.login-box > form > div:nth-child(1) > div > div.el-input > input")
        elem.send_keys(self.user)
        elem = browser.find_element_by_css_selector(
            "#app > div > div.box-flex-6 > div > div.login-box > form > div:nth-child(2) > div > div.el-input > input")
        elem.send_keys(self.password)
        elem = browser.find_element_by_css_selector(
            "#app > div > div.box-flex-6 > div > div.login-box > form > div:nth-child(3) > div > button")
        elem.click()
        # sleep(10)
