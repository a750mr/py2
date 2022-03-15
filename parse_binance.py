import time
import math
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
browser.get("https://www.google.com/")
time.sleep(3)

try:
    header_value = browser.find_element(By.CSS_SELECTOR, ".gLFyf")
    header_value.send_keys("Example python")
    go_search = browser.find_element(By.XPATH, "//input[@aria-label='Поиск в Google'][2]")
    go_search.click()
finally:
    time.sleep(3)
    browser.quit()
# try:
#     treasure = browser.find_element(By.ID, "treasure")
#     answer = browser.find_element(By.ID, "answer")
#     answer.send_keys(response)
#     checkbox = browser.find_element(By.ID, "robotCheckbox")
#     checkbox.click()
#     radiobox = browser.find_element(By.ID, "robotsRule")
#     radiobox.click()
#     button = browser.find_element(By.CSS_SELECTOR, "button.btn")
#     button.click()



