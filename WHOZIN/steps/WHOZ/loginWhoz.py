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


@given(u'Launch Chrome Browser')
def UserIsOnLoginPage(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()


@when(u'Open the Login Page')
def UserIsOnLoginPage(context):
    context.driver.get("https://uat.app.whoz.co")
    time.sleep(3)


@then(u'Verify if the correct login page is opened')
def step_impl(context):
    login_page = context.driver.find_element(By.XPATH, '//*[@id="navbar"]/div/div/div[2]/button[1]').text
    if login_page == "Log In":
        print("Navigated to Login Page Successfully")
    else:
        print("Unable to Navigate to Login Page")
        quit()


@then(u'Verify if the Google Login is working')
def step_impl(context):
    login_with_google = context.driver.find_element(By.XPATH,
                                                    '//*[@id="root"]/div[2]/div/main/div[2]/div/div/div/div/div[1]/form/div[2]/button')
    login_with_google.click()
    time.sleep(4)

    google_email = context.driver.find_element(By.XPATH, '//*[@id="identifierId"]')
    google_email.send_keys("nahmed@technologyrivers.com")
    time.sleep(2)

    click_next_button = context.driver.find_element(By.XPATH, '//*[@id="identifierNext"]/div/button/span')
    click_next_button.click()
    time.sleep(3)

    email_password = context.driver.find_element(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input')
    email_password.send_keys('Hunzai@123')
    time.sleep(2)

    context.driver.find_element(By.XPATH, '//*[@id="passwordNext"]/div/button/span').click()
    time.sleep(5)
    #
    # # cont_with_email_toaster = context.driver.find_element(By.ID,
    # #                                                       'cancel-button')
    # # cont_with_email_toaster.click()
    # time.sleep(2)

    click_continue_button = context.driver.find_element(By.XPATH,
                                                        '/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[3]/div/div/div[2]/div/div/button/span')
    click_continue_button.click()
    time.sleep(5)

    email_after_login = context.driver.find_element(By.XPATH, '//*[@id="navbar"]/div/div/div[2]/div[2]/div/div/span')
    if email_after_login == 'nahmed@technologyrivers.com':
        print("Google Login Is Successful")

    else:
        print("Google Login Failed")
        time.sleep(2)

    context.driver.quit()
