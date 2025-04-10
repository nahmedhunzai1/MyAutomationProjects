from lib2to3.pgen2 import driver

from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from behave import *
from selenium.webdriver.common.by import By
import logging
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--incognito")
driver_path = "../../driver/chrome-mac-arm64/Google Chrome for Testing.app"


@given(u'Launch Chrome Browser1')
def UserIsOnLoginPage(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()


@when(u'Open the Login Page1')
def UserIsOnLoginPage(context):
    context.driver.get("https://uat.app.whoz.co")
    time.sleep(3)


@then(u'Verify if the correct login page is opened1')
def step_impl(context):
    login_page = context.driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div/main/div[2]/div/div/div/div/div[1]/form/div[1]/div/h2').text
    if login_page == "Sign In":
        print("Navigated to Login Page Successfully")
    else:
        print("Unable to Navigate to Login Page")
        quit()


@then(u'Verify if Manual Login is working1')
def step_impl(context):
    input_email = context.driver.find_element(By.XPATH, '//*[@id="email"]')
    input_email.send_keys('nahmed+1@technologyrivers.com')


    password = context.driver.find_element(By.ID,'password')
    password.send_keys('Admin@123')

    sign_in_button = context.driver.find_element(By.XPATH,'//*[@id="root"]/div[2]/div/main/div[2]/div/div/div/div/div[1]/form/div[7]/button')
    sign_in_button.click()
    time.sleep(5)

    recent_notifications= context.driver.find_element(By.XPATH,'//*[@id="root"]/div[2]/div/div/div[2]/div/div[2]/div[2]/div/div[1]/div[1]').text
    if recent_notifications == 'Recent Notifications':
        print(recent_notifications)
        print("Successfully Navigated to Dashboard")
    else:
        assert False, "Unable to Navigate to the Dashboard"

    context.driver.quit()









