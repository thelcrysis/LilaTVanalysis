from bs4 import BeautifulSoup
from selenium import webdriver
import time
url = 'https://lichess.org/tv'

browser = webdriver.Firefox()
browser.get(url)
for i in range(10):
    time.sleep(3)
    print(browser.find_element_by_class_name("number").text)
browser.close()
