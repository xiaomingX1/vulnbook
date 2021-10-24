#coding=utf-8
from typing import Text
from selenium import webdriver
import os,time,sys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait

## 20211024 - 自动化翻译（英文到中文）
def main(keywords):
    ##headless
    chrome_driver = '/Users/yourName/Downloads/chromedriver'  #chromedriver的文件位置
    options=webdriver.ChromeOptions()
    options.add_argument("blink-settings=imagesEnabled=false")
    options.add_argument('--disable-gpu')
    options.add_argument('--hide-scrollbars')
    options.add_argument('--headless')
    chrome_driver = '/Users/yourName/Downloads/chromedriver'  #chromedriver的文件位置
    driver=webdriver.Chrome(options=options,executable_path = chrome_driver)

    driver.get("https://translate.alibaba.com/")

    time.sleep(0.5)
    driver.find_element_by_xpath('//*[@id="original"]').click()
    driver.find_element_by_xpath('//*[@id="original"]').send_keys(keywords)
    driver.find_element_by_xpath('/html/body/div[1]/div[1]/a[1]').click()
    time.sleep(0.5)
    title = driver.find_element_by_xpath('//*[@id="translation-show"]').text
    print(title)
    driver.quit()

main("i love you")
