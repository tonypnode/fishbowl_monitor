from selenium import webdriver
import unittest


class fishBowlWebVisit(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit();




    def test_can_get_fishbowl_page(self):
        self.browser.get('http://127.0.0.1:8000/fishbowl')

        self.assertIn('Hello', self.browser.title)
