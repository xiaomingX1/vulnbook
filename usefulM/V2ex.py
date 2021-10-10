#coding=utf-8
## 说明：
## 【20190719】每日监控与爬取vv2ex中的灌水信息。
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys  #需要引入keys包
import os,time,sys
import time

# 【20211001】现在还用不了，坏了。
# 【20211009】现在还用不了，坏了。
# 【20211010】恢复了，运行环境python3

# reload(sys)
# sys.setdefaultencoding('utf-8')
def main(keywords,url):
    chrome_driver = '/Users/yourName/Downloads/chromedriver'  #chromedriver的文件位置
    # headless
    options=webdriver.ChromeOptions()
    # 提高效率
    options.add_argument("blink-settings=imagesEnabled=false")
    options.add_argument('--disable-gpu')
    options.add_argument('--hide-scrollbars')
    # options.add_argument('--headless')

    options.add_argument('user-agent="Mozilla/5.0 (iPod; U; CPU iPhone OS 2_1 like Mac OS X; ja-jp) AppleWebKit/525.18.1 (KHTML, like Gecko) Version/3.1.1 Mobile/5F137 Safari/525.20"')

    driver=webdriver.Chrome(options=options,executable_path = chrome_driver)
    #driver = webdriver.Chrome()

    driver.get(url)
    for i in range(3):
        time.sleep(0.6)
        js="var q=document.documentElement.scrollTop=10000"
        driver.execute_script(js)

    titles = driver.find_elements_by_xpath('//*[@id="Wrapper"]/div/div[1]/div/table/tbody/tr/td[3]/span[2]/a')
    print(len(titles))
    for i in range(len(titles)):
        print("["+keywords+"]"+titles[i].text + "- " + titles[i].get_attribute("href") )
    time.sleep(10)
    driver.quit()

start = time.time()
main("技术","https://www.v2ex.com/?tab=tech")
# main("创意","https://www.v2ex.com/?tab=creative")
# main("苹果","https://www.v2ex.com/?tab=apple")
# main("工作","https://www.v2ex.com/?tab=jobs")
# main("交易","https://www.v2ex.com/?tab=deals")
end = time.time()
print(end-start)
