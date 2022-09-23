from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions() 
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
# url = 'https://www.baidu.com'
# driver.get(url)

# time.sleep(5)
# input = driver.find_element(By.ID, 'kw')
# input.send_keys('周杰伦')
# time.sleep(5)
# button = driver.find_element(By.ID, 'su')
# button.click
# time.sleep(5)
# js_bottom = 'document.documentElement.scrollTop=100000'
# driver.execute_script(js_bottom)
# time.sleep(2)

url = 'https://www.google.com/'
driver.get(url)

time.sleep(2)
input = driver.find_element(By.NAME, 'q')
input.send_keys('周杰伦')
time.sleep(2)
input.send_keys(Keys.RETURN)
time.sleep(3)
js_bottom = 'document.documentElement.scrollTop=100000'
driver.execute_script(js_bottom)
time.sleep(2)
driver.back()
time.sleep(2)
driver.forward()
time.sleep(2)
driver.quit()