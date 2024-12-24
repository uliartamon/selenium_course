import time
import math

from selenium import webdriver
from selenium.webdriver.common.by import By


URL = 'https://suninjuly.github.io/get_attribute.html'

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


with webdriver.Chrome() as browser:

    browser.get(URL)

    x = browser.find_element(By.CSS_SELECTOR, '#treasure').get_attribute('valuex')
    y = calc(x)

    browser.find_element(By.CSS_SELECTOR, '#answer').send_keys(y)

    browser.find_element(By.CSS_SELECTOR, '#robotCheckbox').click()
    browser.find_element(By.CSS_SELECTOR, '#robotsRule').click()
    browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()

    time.sleep(5)