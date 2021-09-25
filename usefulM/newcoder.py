#coding=utf-8
from selenium import webdriver
import os,time,sys
import time
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
reload(sys)
sys.setdefaultencoding('utf-8')
# 【20210925】爬取牛客网获取最新咨询信息，可自己加规则去掉不关注内容。


def main():
    ##headless
    chrome_driver = '/Users/yourApp/Downloads/chromedriver'  #chromedriver的文件位置
    options=webdriver.ChromeOptions()
    options.add_argument("blink-settings=imagesEnabled=false")
    options.add_argument('--disable-gpu')
    options.add_argument('--hide-scrollbars')
    options.add_argument('--headless')

    # options.add_argument('user-agent="Mozilla/5.0 (iPod; U; CPU iPhone OS 2_1 like Mac OS X; ja-jp) AppleWebKit/525.18.1 (KHTML, like Gecko) Version/3.1.1 Mobile/5F137 Safari/525.20"')

    driver=webdriver.Chrome(chrome_options=options,executable_path = chrome_driver)

    for ii in range(0,20):
        driver.get("https://www.nowcoder.com/discuss?type=0&order=7&pageSize=100&expTag=0&page="+str(ii))
        titles = driver.find_elements_by_xpath('//div[1]/div[2]/div[3]/div/div[5]/ul/li/div//div[1]/a[1]')
        links = driver.find_elements_by_xpath('//div[1]/div[2]/div[3]/div/div[5]/ul/li/div//div[1]/a[1]')
        for i in range(len(titles)):
            if len(titles[i].text) > 12 and not isSpan(titles[i].text):
                print(titles[i].text)
                #print(titles[i].text + " - " + links[i].get_attribute("href").split("?")[0])
    driver.quit()

def isSpan(mtitle):
    # 长度太短，概率是灌水
    if len(mtitle) <= 12:
        return(True)

    # 灌水词屏蔽
    spanList  = ["已认证","置顶"]
    for item in spanList:
        if item in mtitle:
            return(True)
    return(False)

main()

