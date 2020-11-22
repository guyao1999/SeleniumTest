
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


def read_table(file="Keyword.xlsx",sheet_index=0):
    data=xlrd.open_workbook(file)     #打开工作书得到数据
    table=data.sheets()[sheet_index]  #将工作书中的第0也页转换成一个表
    nrows=table.nrows                #得到表的行数i
    list=[]
    for i in range(1,nrows):
        list.append(table.row_values(i))#取出表中的一行存放在list中
    return list

#打开网址并进行搜索
def openBrowser(firstParam,secondParam):
    driver.get(url=firstParam+"/")
    driver.find_element(By.ID,"kw").clear()
    driver.find_element(By.ID,"kw").send_keys(firstParam)
    driver.find_element(By.ID,"su").click()

#跳转到下一页
def goNextPage():
    #driver.find_element(By.LINK_TEXT,u"下一页").click()
    driver.find_element(By.CLASS_NAME,"n").click()


#选取搜索结果中的一项
def select(firstParam,secondParam):
    list=driver.find_elements(By.XPATH,'//div/h3/a')
    if firstParam:
        list[int(firstParam)-1].click()
        time.sleep(2)
    if secondParam:
        list[int(secondParam)-1].click()

#按照关键字执行测试任务
def doTestJob(job):
    jobType=job[0]
    if jobType=='open':
        openBrowser(job[1],job[2])
    elif jobType=='nextPage':
        goNextPage()
    elif jobType=='selectItem':
        select(job[1],job[2])
if __name__=='__main__':
    driver=webdriver.Firefox()
    list=read_table()
    for k in range(len(list)):
        job=list[k]
        doTestJob(job)
        time.sleep(5)
    time.sleep(20)
    driver.quit()