#coding=utf-8
## 说明：
## 【20190129】查询浦发飞客平台情报信息
## 【20210925】更新最新版本并且添加灌水词屏蔽
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys  #需要引入keys包
import os,time,sys
import time
reload(sys)


sys.setdefaultencoding('utf-8')
def main(url,moreinfo):
    ##headless
    chrome_driver = '/Users/yourName/Downloads/chromedriver'  #chromedriver的文件位置
    options=webdriver.ChromeOptions()
    options.add_argument("blink-settings=imagesEnabled=false")
    options.add_argument('--disable-gpu')
    options.add_argument('--hide-scrollbars')
    options.add_argument('--headless')
    driver=webdriver.Chrome(chrome_options=options,executable_path = chrome_driver)
    #driver = webdriver.Chrome()

    driver.get(url)
    js="var q=document.documentElement.scrollTop=10000"
    driver.execute_script(js)
    for i in range(3):
        time.sleep(0.7)
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH ,('//*[@id="autopbn"]'))))
            driver.find_element_by_xpath('//*[@id="autopbn"]').click()
        except:
            print("ERROR!!!!")

    titles = driver.find_elements_by_xpath("//tr/td/div/h2/div/span/a[2]")
    for i in range(len(titles)):
        if not isSpan(titles[i].text):

        #if "删帖" not in titles[i].text and "【" not in titles[i].text and "广告" not in titles[i].text:
            #print("["+moreinfo +"]"+titles[i].text+" - " + titles[i].get_attribute("href"))
            print(titles[i].text)
    driver.quit()

def isSpan(mtitle):
    # 长度太短，概率是灌水
    if len(mtitle) <= 12:
        return(True)

    # 灌水词屏蔽
    spanList  = ["删帖","广告","#",">>","【飞客福利】","福利嗨不停","招募","难","各位"]
    for item in spanList:
        if item in mtitle:
            return(True)
    return(False)

# main("https://www.flyert.com/forum-priorityclub-1.html","IHG")
# main("https://www.flyert.com/forum-marriott-1.html","万豪")
# main("https://www.flyert.com/forum-Hilton-1.html","希尔顿")
# main("https://www.flyert.com/forum-Donghang-1.html","东航")
# main("https://www.flyert.com/forum-HainanAirlines-1.html","海航")
# main("https://www.flyert.com/forum-ChinaSouthern-1.html","南航")
# main("https://www.flyert.com/forum-Cathaypacific-1.html","国泰")
main("https://www.flyert.com/forum-pufa-1.html","浦发")
main("https://www.flyert.com/forum-zhaoshang-1.html","招行")
main("https://www.flyert.com/forum-guangfa-1.html","广发")
main("https://www.flyert.com/forum-zhongxin-1.html","中信")
main("https://www.flyert.com/forum-zhonghang-1.html","中行")
main("https://www.flyert.com/forum-xingye-1.html","兴业") ##  ok
main("https://www.flyert.com/forum-nongye-1.html","农业") ## ok
main("https://www.flyert.com/forum-jianshe-1.html","建行") ## ok
main("https://www.flyert.com/forum.php?mod=forumdisplay&fid=419","光大") ## ok
main("https://www.flyert.com/forum.php?mod=forumdisplay&fid=388","汇丰") ## ok
main("https://www.flyert.com/forum.php?mod=forumdisplay&fid=416","平安") ## ok
main("https://www.flyert.com/forum.php?mod=forumdisplay&fid=323","交通") ## ok
main("https://www.flyert.com/forum.php?mod=forumdisplay&fid=418","邮储") ## ok


