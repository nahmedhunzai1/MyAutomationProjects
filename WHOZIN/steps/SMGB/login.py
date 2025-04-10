from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from behave import *
from selenium.webdriver.common.by import By
import logging

driver_path = "../driver/chrome-mac-arm64/Google Chrome for Testing.app/Contents/MacOS/Google Chrome for Testing"


@given('launch chrome browser')
def UserIsOnLoginPage(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()


@When('User goes to the login page')
def UserIsOnLoginPage(context):
    context.driver.get("https://qa.portal.admin.scanmygolfball.com/login")
    time.sleep(3)


@when('Enter username "{user}" and password "{pwd}"')
def EnterCreds(context, user, pwd):
    context.driver.find_element(By.ID, "outlined-adornment-email-login").send_keys(user)
    context.driver.find_element(By.ID, "outlined-adornment-password-login").send_keys(pwd)
    logging.debug('This is a debug message')
    time.sleep(3)


@when(u'Click on Login button')
def step_impl(context):
    context.driver.find_element(By.XPATH,
                                '//*[@id="root"]/div/div/div/div[1]/div/div/div/div/div/div[3]/form/div[3]/div/button').click()
    time.sleep(8)


@then(u'User must login successfully to the dashboard page')
def step_impl(context):
    try:
        text = context.driver.find_element(By.XPATH, '//*[@id="root"]/div/nav/div/div/div[2]/ul/a[1]/div[2]/h5').text
    except:
        context.driver.close()
        assert False, "TestCase Failed"
    if text == "Dashboard":
        context.driver.close()
        assert True, "TestCase Passed"


@when('user click user section')
def ClickUser(context):
    context.driver.find_element(By.XPATH, '/html/body/div/div/nav/div/div/div[2]/ul/a[3]/div[2]').click()
    time.sleep(4)


@then('User must go to users page')
def step_impl(context):
    try:
        text2 = context.driver.find_element(By.XPATH, '/html/body/div/div/nav/div/div/div[2]/ul/a[3]/div[2]/h5').text
    except:
        context.driver.close()
        assert False, "TestCase Failed"
    if text2 == "Users":
        context.driver.close()
        assert True, "TestCase Passed"


@when(u'user click on date filter')
def step_impl(context):
    users_section = context.driver.find_element(By.XPATH, '/html/body/div/div/nav/div/div/div[2]/ul/a[3]/div[2]')
    users_section.click()
    time.sleep(4)

    from_date = context.driver.find_element(By.XPATH, '/html/body/div/div/main/div/div[1]/div/div[1]')

    from_date.click()
    time.sleep(4)

    next_button = context.driver.find_element(By.NAME, 'Previous month')
    next_button.click()
    # time.sleep(5)
    # required_year = context.driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[1]/div/div/div[1]/div[1]')
    # while required_year.text != 'June 2023':
    #     next_button.click()


@when(u'user selects the desired date')
def step_impl(context):
    context.driver.find_element(By.XPATH,
                                '/html/body/div[2]/div[2]/div[1]/div/div/div[2]/div/div[2]/div/div[3]/button[3]').click()

    date = context.driver.find_element(By.XPATH,
                                       '/html/body/div[2]/div[2]/div[1]/div/div/div[2]/div/div[2]/div/div[3]/button[3]')
    date.click()
