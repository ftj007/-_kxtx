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

        driver.find_element_by_xpath(
            '//*[@id="loginZtcForm"]/div/p[1]/input').send_keys('tjkxadmin')
        driver.find_element_by_xpath(
            '//*[@id="loginZtcForm"]/div/p[2]/input').send_keys('11111111')
        driver.find_element_by_xpath('//*[@id="loginFormSubmit"]').click()
        sleep(3)
        h1 = driver.current_window_handle
        print(h1)
        sleep(3)

        """开单测试"""
        driver.find_element_by_xpath(
            '//*[@id="a_8d23faa9-16a2-4557-889b-3220d198e5c6"]').click()

        mouse_1 = driver.find_element_by_xpath(
            '//*[@id="a_72e6c313-bae4-47f5-9c44-5c4607160c91"]')
        mouse_2 = driver.find_element_by_xpath(
            '//*[@id="menu_list_4"]/div[1]/div[1]')
        ActionChains(driver).move_to_element(
            mouse_1).move_to_element(mouse_2).perform()
        driver.find_element_by_xpath(
            '//*[@id="a_c7a898f2-099a-4619-831f-cc113a112151"]').click()
        sleep(5)

        driver.switch_to.frame('frame_c7a898f2-099a-4619-831f-cc113a112151')

        driver.find_element_by_xpath(
            '/html/body/div[1]/div/div[1]/div/ul/li[1]').click()
        sleep(5)

        iframe = driver.find_element_by_xpath(
            '/html/body/div[1]/div/div[2]/div[1]/iframe')
        driver.switch_to.frame(iframe)

        # 选择所有的checkbox并全部勾上
        # tr = driver.find_elements_by_xpath('//*[@id="content"]/div/div[1]/div[1]/div[2]/table/tbody/tr')
        # print(len(tr))

        # for i in range(1,len(tr)+1):
        #     checkbox = driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div[1]/div[2]/table/tbody/tr[%d]/td[1]' % i)
        #     checkbox.click()
        #     sleep(1)

        driver.find_element_by_xpath(
            '//*[@id="content"]/div/div[1]/div[1]/div[2]/table/tbody/tr[1]/td[1]').click()

        driver.find_element_by_xpath(
            '//*[@id="content"]/form/div[2]/div/div[5]/div[3]/div/input').click()
        sleep(1)
        driver.find_element_by_xpath(
            '//*[@id="tab_listOutSource"]/ul[6]/li[1]').click()
        sleep(1)
        driver.find_element_by_xpath(
            '//*[@id="content"]/div/div[1]/div[1]/div[2]/table/tbody/tr[1]/td[8]/span/div/span').click()
        sleep(5)

        """释放掉所有iframe"""
        driver.switch_to.default_content()
        """再次进入iframe"""
        driver.switch_to.frame('frame_c7a898f2-099a-4619-831f-cc113a112151')

        # t = driver.find_elements_by_xpath('//*[@class="kx-ec-msg-dialog"]')
        # print(len(t))

        driver.find_element_by_xpath(
            '/html/body/div[11]/div/div[3]/button').click()

        # driver.switch_to.default_content()

        frame = driver.find_element_by_xpath(
            '/html/body/div[6]/div/div[2]/iframe')

        driver.switch_to.frame(frame)

        driver.find_element_by_xpath('//*[@id="endStationCode"]').click()
        sleep(1)
        driver.find_element_by_xpath(
            '/html/body/div[3]/div/div[1]/div[1]/ul/li[1]').click()
        sleep(1)
        driver.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/ul/li[1]').click()
        sleep(5)

        driver.find_element_by_xpath(
            '//*[@id="endStationCode"]').click()
        sleep(1)
        driver.find_element_by_xpath(
            '/html/body/div[3]/div/div[3]/ul/li[1]').click()
        sleep(1)
        driver.find_element_by_xpath(
            '//*[@id="content"]/div[1]/div[1]/div[7]/div/input').click()


# //*[@id="content"]/div/div[1]/div[1]/div[2]/table/tbody/tr[1]/td[1]/div/a
# //*[@id="content"]/div/div[1]/div[1]/div[2]/table/tbody/tr[2]/td[1]/div/a
        # 打印当前页面上有多少个checkbox


if __name__ == '__main__':
    unittest.main()
