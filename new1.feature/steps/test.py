import time

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
use_step_matcher("re")


@given("the user is in the registration page")
def step_impl(context):

    driver.get("https://rahulshettyacademy.com/loginpagePractise/")


@when("they enter valid registration details")
def step_impl(context):
    user = driver.find_element(By.XPATH, "//input[@name='username']")
    user.send_keys("rahul")
    driver.find_element(By.XPATH, "//input[@name='password']").send_keys("Rahul@3321")
@step("click the registration button")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    driver.find_element(By.XPATH, "//input[@name='terms']").click()



@then("They should be registered successfully")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    driver.close()


