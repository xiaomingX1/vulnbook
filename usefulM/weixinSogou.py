#coding=utf-8
from typing import Text
from selenium import webdriver
import os,time,sys
import time
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait


# 【20191001】现在还用不了,坏的.
# 【20211017】微信搜索相关关键内容.

def main(keyword):
    ##headless
    options=webdriver.ChromeOptions()
    #options.add_extension("/Users/yourName/Downloads/xzmf.crx")
    options.add_argument("blink-settings=imagesEnabled=false")
    options.add_argument('--disable-gpu')
    options.add_argument('--hide-scrollbars')
    options.add_argument('--headless')

    #options.add_argument('user-agent="Mozilla/5.0 (iPod; U; CPU iPhone OS 2_1 like Mac OS X; ja-jp) AppleWebKit/525.18.1 (KHTML, like Gecko) Version/3.1.1 Mobile/5F137 Safari/525.20"')
    #options.add_argument(r'user-data-dir=/Users/yourName/Library/Application Support/Google/Chrome/UserDataForSelenium20211002')
    chrome_driver = '/Users/yourName/Downloads/chromedriver'  #chromedriver的文件位置
    driver=webdriver.Chrome(options=options,executable_path = chrome_driver)

    #driver = webdriver.Chrome()
    for ii in range(1,2):
        murl = "https://weixin.sogou.com/weixin?_sug_type_=&sut=5845&s_from=input&_sug_=n&type=2&sst0=1634479137107&page=%s&ie=utf8&w=01019900&dr=1&query=%s"%(str(ii),keyword)        
        driver.get(murl)

        for i in range(3):
            js="var q=document.documentElement.scrollTop=1000000"
            driver.execute_script(js)
            time.sleep(0.6)

        titles = driver.find_elements_by_xpath('//*[contains(@id,"title")]')
        for i in range(len(titles)):
            print(titles[i].text.strip() + " - " + titles[i].get_attribute("href"))
            #print(titles[i].text + " - " + recommend[i].Text + " - " + links[i].get_attribute("href"))
    driver.quit()
main("javax.script.ScriptEngine.eval")
#print('https://weixin.sogou.com/weixin?_sug_type_=&sut=5845&s_from=input&_sug_=n&type=2&sst0=1634479137107&page=%s&ie=utf8&w=01019900&dr=1&query='%'333')


