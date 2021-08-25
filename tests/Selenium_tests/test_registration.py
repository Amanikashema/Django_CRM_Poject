from selenium import webdriver
from django.test import LiveServerTestCase, TransactionTestCase
from selenium.webdriver.common.keys import Keys
import time


# class for registration
class TestRegistrationPage(LiveServerTestCase):
    def setup(self):
        path = "C:\Program Files (x86)\chromedriver.exe"
        self.driver = webdriver.Chrome(path)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def test_registration(self):
        self.setup()
        self.driver.get(self.live_server_url)
        sign_up_button = self.driver.find_element_by_class_name("ml-2")
        print(sign_up_button)






    def teardown(self):
        self.driver.quit()


