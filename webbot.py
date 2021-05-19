from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
mydriver = webdriver.Chrome()
mydriver.get("http://www.speedcheck.ir/")
print(mydriver.title)
print(mydriver.current_url)
mydriver.find_element_by_xpath("/html/body/div[2]/div[3]/button[2]").click()
mydriver.find_element_by_xpath("/html/body/div[2]/div[2]/div/h1").click()
time.sleep(5)
# mydriver.back()
# mydriver.close()