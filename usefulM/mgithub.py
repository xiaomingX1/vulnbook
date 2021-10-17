#coding=utf-8
## 说明：
## 【20190719】爬去juejin看别人在讨论什么新鲜事情。
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys  #需要引入keys包
import os,time,sys
import time

# 20211017 - 更新代码.


def main(keyword):
    # headless
    options=webdriver.ChromeOptions()
    # 提高效率
    chrome_driver = '/Users/Yourname/Downloads/chromedriver'  #chromedriver的文件位置
    options.add_argument("blink-settings=imagesEnabled=false")
    options.add_argument('--disable-gpu')
    options.add_argument('--hide-scrollbars')
    options.add_argument('--headless')
    driver=webdriver.Chrome(options=options,executable_path = chrome_driver)
    #driver = webdriver.Chrome()
    for mpage in range(1,5):
        print("https://github.com/search?o=desc&q=%s&s=stars&type=Repositories&p=%s"%(keyword,str(mpage)))
        driver.get("https://github.com/search?o=desc&q=%s&s=stars&type=Repositories&p=%s"%(keyword,str(mpage)))
        for i in range(1,2):
            time.sleep(0.6)
            js="var q=document.documentElement.scrollTop=30000"
            driver.execute_script(js)

        titles = driver.find_elements_by_xpath('//*[@id="js-pjax-container"]/div/div[3]/div/ul/li/div[2]/div[1]/div/a')
        profiles = driver.find_elements_by_xpath('//*[@id="js-pjax-container"]/div/div[3]/div/ul/li/div[2]/div[2]/div')
        jj = 0
        for i in range(len(titles)):
            print("["+str(i)+"]"+titles[i].text + " - " + titles[i].get_attribute("href"))
            while (len(profiles) > jj and "Updated" not in profiles[jj].text):
                jj = jj + 1
            try:
                print("["+str(i)+"]"+profiles[jj].text.replace("\n","-").replace(" ","").replace("Updated","Updated-"))
            except:
                print("Error + continue ... ")
            jj = jj + 1
            print("=======================")
    time.sleep(1)
    driver.quit() 

start = time.time()
#main("java")
main("telegram")
end = time.time()
print("总消耗时间:"+str(end-start))
