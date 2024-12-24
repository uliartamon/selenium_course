import time


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

URL = 'https://suninjuly.github.io/selects1.html'

with webdriver.Chrome() as browser:

    browser.get(URL)

    x = int(browser.find_element(By.CSS_SELECTOR, '#num1').text)
    y = int(browser.find_element(By.CSS_SELECTOR, '#num2').text)

    res = x + y

    select = Select(browser.find_element(By.CSS_SELECTOR, '#dropdown'))
    select.select_by_value(str(res))

    browser.find_element(By.CSS_SELECTOR, '[class="btn btn-default"]').click()
    
    time.sleep(10)
