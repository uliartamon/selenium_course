import time
import os

from selenium import webdriver
from selenium.webdriver.common.by import By


URL = 'https://suninjuly.github.io/file_input.html'

directory = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(directory, 'output.txt')


print(file_path)
info = ['Elena', 'Vorontsova', 'voron_elen@pipu.com']

with webdriver.Chrome() as browser:

    browser.get(URL)

    info_form = browser.find_elements(By.CSS_SELECTOR, '.form-group input')
    for i, el in enumerate(info_form):
        el.send_keys(info[i])

    browser.find_element(By.CSS_SELECTOR, '#file').send_keys(file_path)
    

    browser.find_element(By.CSS_SELECTOR, '[class="btn btn-primary"]').click()
    time.sleep(5)


print("OKOKOKOKOK")