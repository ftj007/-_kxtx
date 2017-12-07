from selenium import webdriver
from selenium.webdriver.common.by import By
import os,time


base_url = 'https://www.baidu.com'
base_path = os.path.dirname(os.path.abspath(__file__)) + '\..'
print(base_path)
print(os.path.abspath(__file__))
driver_path = os.path.abspath(base_path+'\drivers\chromedriver.exe')
print(driver_path)

locator_kw = (By.ID, 'kw')
locator_su = (By.ID, 'su')
locator_result = (By.XPATH, '//div[contains(@class, "result")]/h3/a')


driver = webdriver.Chrome(executable_path = driver_path)
driver.get(base_url)
driver.find_element(*locator_kw).send_keys('selenium')
# driver.find_element(by = By.ID,value = 'kw').send_keys('selenium')
driver.find_element(*locator_su).click()
time.sleep(2)
links = driver.find_elements(*locator_result)
for link in links:
    print(link.text)
driver.quit()





