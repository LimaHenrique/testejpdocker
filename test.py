import unittest
from unittest import TestCase
from selenium import webdriver
from pages.pages.pageObject import Home

class TestPageHome(TestCase):

    def setUp(self):
        self.driver=webdriver.Chrome('driver/chromedriver')
        self.page_home=Home(self.driver)
        self.driver.get('https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin')

    def test_navigate(self):
        assert self.driver.title == 'Gmail'

    def tearDown(self):
        self.driver.close()
if __name__ == "__main__":
    unittest.main()
