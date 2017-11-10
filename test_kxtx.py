from selenium import webdriver
import unittest
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

class KXTX(unittest.TestCase):

    def setUp(self):
        self.base_url = 'https://pet-sso.kxtx.cn/html/login/login'
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)

    def tearDown(self):
        self.driver.quit()

    def test_login(self):
        """登录测试"""
        driver = self.driver
        self.driver.maximize_window()
        driver.get(self.base_url)

        driver.find_element_by_xpath('//*[@id="loginZtcForm"]/div/p[1]/input').send_keys('tjkxadmin')
        driver.find_element_by_xpath('//*[@id="loginZtcForm"]/div/p[2]/input').send_keys('11111111')
        driver.find_element_by_xpath('//*[@id="loginFormSubmit"]').click()
        sleep(3)
        h1 = driver.current_window_handle
        print(h1)
        sleep(3)

        """开单测试"""
        driver.find_element_by_xpath('//*[@id="a_8d23faa9-16a2-4557-889b-3220d198e5c6"]').click()

        mouse_1 = driver.find_element_by_xpath('//*[@id="a_72e6c313-bae4-47f5-9c44-5c4607160c91"]')
        mouse_2 = driver.find_element_by_xpath('//*[@id="menu_list_4"]/div[1]/div[1]')
        ActionChains(driver).move_to_element(mouse_1).move_to_element(mouse_2).perform()
        driver.find_element_by_xpath('//*[@id="a_c7a898f2-099a-4619-831f-cc113a112151"]').click()
        sleep(5)


        driver.switch_to.frame('frame_c7a898f2-099a-4619-831f-cc113a112151')

        driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/ul/li[1]').click()
        sleep(5)

        iframe = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/iframe')
        driver.switch_to.frame(iframe)

        # driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div[1]/div[2]/table/tbody/tr[1]/td[4]/span/span/a').click()

        # 选择所有的checkbox并全部勾上

        for i in range(1,10):
            checkbox = driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div[1]/div[2]/table/tbody/tr[%d]/td[1]' % i)
            checkbox.click()
            sleep(1)



# //*[@id="content"]/div/div[1]/div[1]/div[2]/table/tbody/tr[1]/td[1]/div/a
# //*[@id="content"]/div/div[1]/div[1]/div[2]/table/tbody/tr[2]/td[1]/div/a
        # 打印当前页面上有多少个checkbox


if __name__ == '__main__':
    unittest.main()
