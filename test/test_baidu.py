from selenium import webdriver
import unittest
from time import sleep
from selenium.webdriver.common.by import By
from utils.config import Config, DRIVER_PATH, DATA_PATH
from utils.log import logger
from utils.file_reader import ExcelReader
import os

class BaiduTest(unittest.TestCase):
    URL = Config().get('URL')
    # excel = DATA_PATH + '/baidu.xlsx'
    excel = os.path.join(DATA_PATH, 'baidu.xlsx')


    locator_kw = (By.ID, 'kw')
    locator_su = (By.ID, 'su')
    locator_result = (By.XPATH, '//div[contains(@class, "result")]/h3/a')

    def sub_setUp(self):
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH + '\chromedriver.exe')
        self.driver.get(self.URL)
        self.driver.implicitly_wait(30)

    # def test_baidu_0(self):
    #     driver = self.driver
    #     driver.find_element(*self.locator_kw).send_keys('selenium')
    #     driver.find_element(*self.locator_su).click()
    #     sleep(2)
    #     links = driver.find_elements(*self.locator_result)
    #     for link in links:
    #         # print(link.text)
    #         logger.debug(link.text)

    # def test_baidu_1(self):
    #     driver = self.driver
    #     driver.find_element(*self.locator_kw).send_keys('unittest')
    #     driver.find_element(*self.locator_su).click()
    #     sleep(2)
    #     links = driver.find_elements(*self.locator_result)
    #     for link in links:
    #         # print(link.text)
    #         logger.debug(link.text)


    def test_search(self):
        datas = ExcelReader(self.excel).data
        for d in datas:
            print(d)
            with self.subTest(data=d):
                 self.sub_setUp()
                 self.driver.find_element(*self.locator_kw).send_keys(d['search'])
                 self.driver.find_element(*self.locator_su).click()
                 sleep(2)
                 links = self.driver.find_elements(*self.locator_result)
                 for link in links:
                     logger.info(link.text)
                 self.sub_tearDown()


    def sub_tearDown(self):
        self.driver.quit()



if __name__ == '__main__':
    unittest.main(verbosity=2)
