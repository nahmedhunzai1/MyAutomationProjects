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
from selenium.webdriver.common.keys import Keys

chrome_options = Options()
chrome_options.add_argument("--incognito")
driver_path = "../../driver/chrome-mac-arm64/Google Chrome for Testing.app"




@given(u'Launch Chrome Browser2')
def UserIsOnLoginPage(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()


@when(u'Open the Login Page2')
def UserIsOnLoginPage(context):
    context.driver.get("https://uat.app.whoz.co")
    time.sleep(3)


@then(u'Verify if the correct login page is opened2')
def step_impl(context):
    login_page = context.driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div/main/div[2]/div/div/div/div/div[1]/form/div[1]/div/h2').text
    if login_page == "Sign In":
        print("Navigated to Login Page Successfully")
    else:
        print("Unable to Navigate to Login Page")
        quit()

@then(u'Invalid email message is appearing')
def step_impl(context):
    print("aksjdlh")
    input_email = context.driver.find_element(By.XPATH, '//*[@id="email"]')
    input_email.send_keys('user@example@domain.com')

    password = context.driver.find_element(By.ID, 'password')
    password.send_keys('Admin@123')

    sign_in_button = context.driver.find_element(By.XPATH,
                                                 '//*[@id="root"]/div[2]/div/main/div[2]/div/div/div/div/div[1]/form/div[7]/button')
    sign_in_button.click()
    time.sleep(1)

    wrong_email_message = context.driver.find_element(By.XPATH,'//*[@id="root"]/div[2]/div/main/div[2]/div/div/div/div/div[1]/form/div[4]/div/p[2]').text
    if wrong_email_message == "Please provide a valid email address":
        print("Invalid email validation message appeared")
    else:
        assert False, "Invalid email validation message is not appearing"
    input_email.send_keys(Keys.COMMAND + "a")
    input_email.send_keys(Keys.DELETE)
    time.sleep(3)




@then(u'Wrong password message is appearing')
def step_impl(context):
    print('asdfad')
    input_email = context.driver.find_element(By.XPATH, '//*[@id="email"]')
    input_email.send_keys('nahmed@technologyrivers.com')

    password = context.driver.find_element(By.ID, 'password')
    password.send_keys('Admin@12311111')

    sign_in_button = context.driver.find_element(By.XPATH,
                                                 '//*[@id="root"]/div[2]/div/main/div[2]/div/div/div/div/div[1]/form/div[7]/button')
    sign_in_button.click()
    time.sleep(1)

#/html/body/div[1]/div[1]/div/div/div[1]/div[2]/div/span


    try:
        toaster_element = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='MuiBox-root']/div/span")))

        toaster_title = toaster_element.text
        print('Toaster element is  ',toaster_element)
    except Exception as e:
        print(e)


    time.sleep(3)











