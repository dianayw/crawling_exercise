from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# path = 'chromedriver.exe'
# driver = webdriver.Chrome(path)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
url = 'https://www.baidu.com'
driver.get(url)
# content = browser.page_source
# print(content)

# 元素定位
# ps 尚硅谷这里教的已经不能用了：.find_element_by_id('') ->LEGACY CODE
element = driver.find_element(By.XPATH, '//input[@id="kw"]')
# .find_element(By.ID, "id")
# .find_element(By.NAME, "name")
# .find_element(By.XPATH, "xpath")
# .find_element(By.LINK_TEXT, "link text")
# .find_element(By.PARTIAL_LINK_TEXT, "partial link text")
# .find_element(By.TAG_NAME, "tag name")
# .find_element(By.CLASS_NAME, "class name")
# .find_element(By.CSS_SELECTOR, "css selector")

# 获取元素信息
# print(element.get_attribute('class'))
# print(element.tag_name)
# print(element.text)
# link = driver.find_element(By.LINK_TEXT,"新闻")
# print(link.text)

# 交互
# .send_keys('abcd') # 输入abcd
# .click # 点击
# time.sleep(2) # 延迟2s
# js_bottom = 'document.documentElement.scrollTop=100000'
# .execute_script(js_bottom) # 向下滑动页面
# driver.back()
# driver.forward()
# driver.quit()
