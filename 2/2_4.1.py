import time

from selenium import webdriver
from selenium.webdriver.common.by import By


URL = 'https://suninjuly.github.io/cats.html'

with webdriver.Chrome() as browser:

    browser.get(URL)

    browser.find_element(By.ID, "button") 

