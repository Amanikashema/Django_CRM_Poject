from selenium import webdriver
from django.test import LiveServerTestCase
from selenium.webdriver.common.keys import Keys
import time


class TestHomePage(LiveServerTestCase):
    def test_login(self):
        path = "C:\Program Files (x86)\chromedriver.exe"
        self.driver = webdriver.Chrome(path)
        # self.driver.get("localhost:8000/login/")
        self.driver.get(self.live_server_url)
        # assert if user is directed to login page title
        self.assertEquals(self.driver.title, 'Login')
        # get form fields
        username_field = self.driver.find_element_by_name('username')
        password_field = self.driver.find_element_by_name('password')
        print(username_field.send_keys("rod"))
        print(password_field.send_keys("Rod@1234"))

        # submit button
        submit_button = self.driver.find_element_by_class_name('login_btn')
        submit_button.send_keys(Keys.RETURN)

        time.sleep(60)
