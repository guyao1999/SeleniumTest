
import pytest
import time
import json
import xlrd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

#打开网址并进行搜索
def openBrowser():
    #打开火狐浏览器
    driver=webdriver.Firefox()

    #进入到百度的页面
    url="http://www.baidu.com"
    driver.get(url)
    #查找到输出框，输入"南京航空航天大学"
    driver.find_element(By.ID,"kw").clear()
    driver.find_element(By.ID,"kw").send_keys("i.nuaa.edu.cn")
    #点击进行检索
    driver.find_element(By.ID,"su").click()

    #判断关键字是否检索到
    time.sleep(10)
    res="南京航空航天大学" in driver.find_element(By.TAG_NAME,("body")).text
    if res:
        print("检索到了")
    else:
        print("没有检索到")
    #print(driver.find_element(By.TAG_NAME,("body")).text)
    #停止一段时间方便查看效果
   
    #关闭浏览器
    driver.quit()
if __name__=='__main__':
    openBrowser()
   