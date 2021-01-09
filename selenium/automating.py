import time
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("start-maximized")
chrome_options.add_argument("--incognito") #using this argument the browser is opened in incognito mode
# chrome_options.headless = True

driver = webdriver.Chrome(chrome_options=chrome_options)


driver.get('https://www.google.com/')
search_box = driver.find_element_by_name('q')
search_box.send_keys('Youtube')
search_box.submit()
driver.refresh()
time.sleep(5)
link = driver.find_element_by_xpath('//*[@id="rso"]/div[1]/div/div/div/div[1]/a/h3/span').click()
# driver.refresh()
# time.sleep(5)
print("\nTitle: "+ str(driver.title))
print("\nURL: "+ str(driver.current_url))
search_box = driver.find_element_by_name('search_query')
print("\nTitle: "+ str(driver.title))
print("\nURL: "+ str(driver.current_url))
search_box.send_keys('Web2py Playlist')
search_box.submit()
print("\nTitle: "+ str(driver.title))
print("\nURL: "+ str(driver.current_url))
time.sleep(1)

link = driver.find_element_by_xpath('//*[@id="video-title"]').click()
time.sleep(1)
print("\nTitle: "+ str(driver.title))
print("\nURL: "+ str(driver.current_url))
link = driver.find_element_by_xpath('//*[@id="movie_player"]/div[24]/div[2]/div[1]/button').click()
time.sleep(1)

link = driver.find_element_by_xpath('//*[@id="movie_player"]/div[24]/div[2]/div[2]/button[9]').click()
time.sleep(1)

link = driver.find_element_by_xpath('//*[@id="movie_player"]/div[24]/div[2]/div[1]/button').click()
time.sleep(1)
