import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/loginpagePractise/")
user=driver.find_element(By.XPATH, "//input[@name='username']")
user.send_keys("rahul")
driver.find_element(By.XPATH, "//input[@name='password']").send_keys("Rahul@3321")
driver.find_element(By.XPATH,"//input[@name='terms']").click()
time.sleep(5)