import time
import math

from selenium import webdriver
from selenium.webdriver.common.by import By


URL = 'https://suninjuly.github.io/execute_script.html'

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


with webdriver.Chrome() as browser:

    browser.get(URL)

    x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
    x = x_element.text
    y = calc(x)
    browser.find_element(By.CSS_SELECTOR, '#answer').send_keys(y)

    submit = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    browser.execute_script("return arguments[0].scrollIntoView(true);", submit)

    browser.find_element(By.CSS_SELECTOR, '#robotCheckbox').click()
    browser.find_element(By.CSS_SELECTOR, '#robotsRule').click()
    submit.click()

    time.sleep(5)


print("OKOKOKOKOK")