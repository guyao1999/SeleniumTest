

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

def read_table(file="search.xlsx",sheet_index=0):
    data=xlrd.open_workbook(file)     #打开工作书得到数
    
    table=data.sheets()[sheet_index]  #将工作书中的第0也页转换成一个表
    nrows=table.nrows                #得到表的行数i
    list=[]
    for i in range(1,nrows):
        list.append(table.row_values(i))#取出表中的一行存放在list中
    return list
 #按照关键字执行测试任务
def doSearchJob(job):

    #进入到百度的页面
    url="http://www.baidu.com"
    driver.get(url)
    #查找到输出框，输入"南京航空航天大学"
    driver.find_element(By.ID,"kw").clear()
    target=job[0]
    result=job[1]
    driver.find_element(By.ID,"kw").send_keys(target)
    #点击进行检索
    driver.find_element(By.ID,"su").click()

    #这里停一段时间，便于观察结果和下行代码获取页面内容留足够的时间
    time.sleep(10)
    #判断关键字是否检索到
    results=driver.find_element(By.TAG_NAME,("body")).text
    #print(results)
    res=result in results
    if res:
        print("检索到了:"+result)
    else:
        print("没有检索到:"+result)
   
    #停止一段时间方便查看效果
  
if __name__=='__main__':
    driver=webdriver.Firefox()
    list=read_table()
    print("打开文件成功")
    for i in range(len(list)):
        job=list[i]
        doSearchJob(job)
    driver.quit()
   