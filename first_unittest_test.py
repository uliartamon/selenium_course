import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


URL_1 = 'https://suninjuly.github.io/registration1.html'
URL_2 = 'https://suninjuly.github.io/registration2.html'


class TestURL(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.wait = WebDriverWait(self.browser, 10)

    def tearDown(self):
        self.browser.quit()

    def fill_forms_and_submit(self, url):

        self.browser.get(url)

        self.browser.find_element(By.CSS_SELECTOR, '.first_block [class="form-control first"]').send_keys('Ivan')
        self.browser.find_element(By.CSS_SELECTOR, '.first_block [class="form-control second"]').send_keys('Berezov')
        self.browser.find_element(By.CSS_SELECTOR, '.first_block [class="form-control third"]').send_keys('BerezovIvan@bk.ru')

        self.browser.find_element(By.CSS_SELECTOR, '[class="btn btn-default"]').click()
        welcome_text = self.browser.find_element(By.TAG_NAME, 'h1').text

        return welcome_text
    
    def test_url1(self):
        welcome_text = self.fill_forms_and_submit(URL_1)
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "URL 1 failed")


    def test_url2(self):
        welcome_text = self.fill_forms_and_submit(URL_2)
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "URL 1 failed")

if __name__ == '__main__':
    unittest.main()