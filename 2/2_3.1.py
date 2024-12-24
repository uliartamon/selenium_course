import time
import math

from selenium import webdriver
from selenium.webdriver.common.by import By


URL = 'https://suninjuly.github.io/alert_accept.html'

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


with webdriver.Chrome() as browser:

    browser.get(URL)
    browser.find_element(By.CSS_SELECTOR, '[class="btn btn-primary"]').click()

    alert = browser.switch_to.alert
    alert.accept()

    x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
    x = x_element.text
    y = calc(x)
    browser.find_element(By.CSS_SELECTOR, '#answer').send_keys(y)

    submit = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    submit.click()

    alert = browser.switch_to.alert
    text = alert.text.split(':')[-1]

print(text)