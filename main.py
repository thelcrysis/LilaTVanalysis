from selenium import webdriver
import time
from time import gmtime, strftime
def scraper(cycles):
    url = 'https://lichess.org/tv'   #lila TV url
    file = open("record.txt","w")    #recorded checks save file

    #changing chromium's options, headless and silent -> log-level
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('--mute-audio')

    #starting chromium as webdriver
    browser = webdriver.Chrome(executable_path='/usr/lib/chromium-browser/chromedriver', chrome_options=options)
    browser.get(url)

    currentNumberofWatcher = 0
    for cycle in range(cycles):
        time.sleep(2)
        if (currentNumberofWatcher != browser.find_element_by_class_name("number").text):
            currentNumberofWatcher = browser.find_element_by_class_name("number").text
            if (currentNumberofWatcher != ''):
                output = (strftime("%d %m %Y %H:%M:%S", gmtime()) + "-" + currentNumberofWatcher)
                print(output)    #<---- prints out whats happening
        else:
            print "-||-"         #<---- this too (one comment above)
        if (currentNumberofWatcher != ''):
            file.write(output + '\n')
    file.close() #wont run if stopped by ctrl+c
    browser.close()
