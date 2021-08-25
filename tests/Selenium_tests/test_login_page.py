from selenium import webdriver
from django.test import LiveServerTestCase, TransactionTestCase
from selenium.webdriver.common.keys import Keys
import time


class TestHomePage(LiveServerTestCase):
    def setup(self):
        path = "C:\Program Files (x86)\chromedriver.exe"
        self.driver = webdriver.Chrome(path)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def test_title(self):
        self.setup()
        self.driver.get(self.live_server_url)
        # assert if user is directed to login page title
        self.assertEquals(self.driver.title, 'Login')

    def test_login(self):
        self.setup()
        self.driver.get(self.live_server_url)
        username_field = self.driver.find_element_by_name('username')
        password_field = self.driver.find_element_by_name('password')
        username_field.send_keys("rod")
        password_field.send_keys("Rod1@1234")
        self.driver.implicitly_wait(40)
        # submit button
        submit_button = self.driver.find_element_by_class_name('login_btn')
        submit_button.click()

    def teardown(self):
        self.driver.quit()