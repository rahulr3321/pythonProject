import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.google.com/")
driver.maximize_window()

text=driver.find_element(By.XPATH,"//textarea[@class='gLFyf']")
