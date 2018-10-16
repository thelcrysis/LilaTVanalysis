from selenium import webdriver
import time
from time import gmtime, strftime
url = 'https://lichess.org/tv'
file = open("fo.txt","a")
browser = webdriver.Firefox()
browser.get(url)
currentNumberofWatcher = 0
while(1):
    time.sleep(2)
    if (currentNumberofWatcher != browser.find_element_by_class_name("number").text):
        currentNumberofWatcher = browser.find_element_by_class_name("number").text
        if (currentNumberofWatcher != None):
            output = (strftime("%d %m %Y %H:%M:%S", gmtime()) + "-> " + currentNumberofWatcher)
            file.write(output + '\n')
            print(output)
    else:
        print "-||-"
fo.close()
browser.close()
