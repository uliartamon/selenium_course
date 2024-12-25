import pytest
import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

URL ='http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_check_basket(browser):
    browser.get(URL)
    time.sleep(30)
    try:
        basket = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'btn-add-to-basket'))
        )
    except NoSuchElementException:
        basket = None
    assert basket is not None, 'Basket was not found'


