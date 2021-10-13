#coding=utf-8
## 说明：
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys  #需要引入keys包
import os,time,sys
import time

def main():
    # headless
    options=webdriver.ChromeOptions()
    # 提高效率
    chrome_driver = '/Users/YourName/Downloads/chromedriver'  #chromedriver的文件位置
    options.add_argument("blink-settings=imagesEnabled=false")
    options.add_argument('--disable-gpu')
    options.add_argument('--hide-scrollbars')
    #options.add_argument('--headless')
    options.add_argument(r'user-data-dir=/Users/yourName/Library/Application Support/Google/Chrome/UserDataForSelenium20211012_weibo')
    driver=webdriver.Chrome(options=options,executable_path = chrome_driver)
    #driver = webdriver.Chrome()

    driver.get("https://weibo.com/u/3960916077")
    for i in range(5):
        time.sleep(1)
        js="var q=document.documentElement.scrollTop=10000"
        driver.execute_script(js)

    jjs = 'ss = document.querySelectorAll(".expand");for (i = 0; i < ss.length; i++) {ss[i].click()}'
    driver.execute_script(jjs)
    time.sleep(1)
    
    ## //*[@id="scroller"]/div[1]/div/div/article/div/div/div[1]/div/span
    titles = driver.find_elements_by_xpath('//*[@id="scroller"]/div[1]/div/div/article/div/div/div[1]/div')
    for i in range(len(titles)):
        print("================")
        print(titles[i].text.replace("收起",""))
    driver.quit()


start = time.time()
main()
end = time.time()
print("总消耗时间:"+str(end-start))
