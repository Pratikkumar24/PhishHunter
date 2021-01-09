import time
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("start-maximized")
chrome_options.add_argument("--incognito") #using this argument the browser is opened in incognito mode
# chrome_options.headless = True    Using this argument you wont get the windows view

driver = webdriver.Chrome(chrome_options=chrome_options)

url = "https://transparencyreport.google.com/safe-browsing/search?hl=en"
driver.get('https://transparencyreport.google.com/safe-browsing/search?hl=en')

searchBox = driver.find_element_by_xpath('//*[@id="scrolling-element"]/safe-browsing-report/ng-component/section/div/search-box/input')
searchBox.send_keys(url)
searchBox= driver.find_element_by_xpath('//*[@id="scrolling-element"]/safe-browsing-report/ng-component/section/div/search-box/i').click()
