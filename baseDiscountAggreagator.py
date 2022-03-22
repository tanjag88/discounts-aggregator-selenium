import unittest
from datetime import datetime
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.service import Service
import datetime
import websiteURLs as urls


class BaseDiscountAggregatorTests(unittest.TestCase):
    s = Service(executable_path='../chromedriver.exe')
    driver = webdriver.Chrome(service=s)

    @classmethod
    def setUpClass(cls):
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(50)
        cls.driver.get(urls.baseUrl)
        print(cls.driver.current_url)
        if cls.driver.current_url == urls.baseUrl:
            print('Successfully launch website home page')
        else:
            print('Something went wrong, try again!')

    @classmethod
    def tearDownClass(cls):
        if cls.driver is not None:
            print(f'The test Completed at: {datetime.datetime.now()}')
            sleep(1)
            cls.driver.close()
            cls.driver.quit()
