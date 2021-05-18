from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
mydriver = webdriver.Chrome()
mydriver.get("https://www.bbc.com/news")
print(mydriver.title)
print(mydriver.current_url)
mydriver.find_element_by_xpath("//*[@id="orb-nav-links"]/ul/li[3]/a").click()
time.sleep(5)
mydriver.close()