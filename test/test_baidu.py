from selenium import webdriver
import unittest
from time import sleep
from selenium.webdriver.common.by import By
from utils.config import Config, DRIVER_PATH
from utils.log import logger

class BaiduTest(unittest.TestCase):
    URL = Config().get('URL')

    locator_kw = (By.ID, 'kw')
    locator_su = (By.ID, 'su')
    locator_result = (By.XPATH, '//div[contains(@class, "result")]/h3/a')

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH + '\chromedriver.exe')
        self.driver.get(self.URL)
        self.driver.implicitly_wait(30)

    def test_baidu_0(self):
        driver = self.driver
        driver.find_element(*self.locator_kw).send_keys('selenium')
        driver.find_element(*self.locator_su).click()
        sleep(2)
        links = driver.find_elements(*self.locator_result)
        for link in links:
            # print(link.text)
            logger.info(link.text)

    def test_baidu_1(self):
        driver = self.driver
        driver.find_element(*self.locator_kw).send_keys('unittest')
        driver.find_element(*self.locator_su).click()
        sleep(2)
        links = driver.find_elements(*self.locator_result)
        for link in links:
            # print(link.text)
            logger.info(link.text)


    def tearDown(self):
        self.driver.quit()



if __name__ == '__main__':
    unittest.main()
