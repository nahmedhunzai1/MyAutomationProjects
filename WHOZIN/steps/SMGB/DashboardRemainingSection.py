import logging
import time

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By

driver_path = "../driver/chrome-mac-arm64/Google Chrome for Testing.app/Contents/MacOS/Google Chrome for Testing"


@given('launched chrome browser3')
def UserIsOnLoginPage(context):
    print('Launching browser')
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()


@When('User navigates to the login page3')
def UserIsOnLoginPage(context):
    context.driver.get("https://qa.portal.admin.scanmygolfball.com/login")
    time.sleep(3)


@when('Enter username3 "{user3}" and password3 "{pwd3}"')
def EnterCreds(context, user3, pwd3):
    context.driver.find_element(By.ID, "outlined-adornment-email-login").send_keys(user3)
    context.driver.find_element(By.ID, "outlined-adornment-password-login").send_keys(pwd3)
    logging.debug('This is a debug message')
    time.sleep(3)


@when(u'Click on Login button3')
def step_impl(context):
    context.driver.find_element(By.XPATH,
                                '//*[@id="root"]/div/div/div/div[1]/div/div/div/div/div/div[3]/form/div[3]/div/button').click()
    time.sleep(2)


@given(u'User is on the Admin Dashboard3')
def step_impl(context):
    dashboard = context.driver.find_element(By.XPATH,
                                            '/html/body/div/div/nav/div/div/div[2]/ul/a[1]/div[2]/h5').text
    if dashboard == "Dashboard":
        print('navigated to Dashboard')
    else:
        print('Dashboard navigation failed')


@when(u'User navigates to Scan per rate of playability section')
def step_impl(context):
    time.sleep(3)
    scans_per_rate_of_playability = context.driver.find_element(By.XPATH,
                                                                '/html/body/div/div/main/div/div/div[2]/div/div[1]/div/div[1]/div[1]/span').text

    time.sleep(2)
    if scans_per_rate_of_playability == 'Scans per rate of playability':
        print('User is successfully navigated to the Scan per rate of playability section')
    else:
        print('Failed to navigate to the Scan per rate of playability section')


@when(u'Changes the from and to dates then the graph is working fine')
def step_impl(context):
    time.sleep(3)

    context.driver.find_element(By.XPATH,
                                '/html/body/div/div/main/div/div/div[2]/div/div[1]/div/div[2]/div/div[2]/div/div/div/div[1]/div[1]').click()
    time.sleep(2)
    var = context.driver.find_element(By.XPATH,
                                      '/html/body/div[2]/div[2]/div[1]/div/div/div[1]/div[1]/div').text
    time.sleep(2)
    back_next_button = context.driver.find_element(By.XPATH,
                                                   '/html/body/div[2]/div[2]/div[1]/div/div/div[1]/div[2]/button[1]')
    time.sleep(2)
    from_year_to_select = context.driver.find_element(By.XPATH,
                                                      '/html/body/div[2]/div[2]/div[1]/div/div/div[1]/div[1]/div').text

    while from_year_to_select != 'February 2023':
        back_next_button.click()
        from_year_to_select = context.driver.find_element(By.XPATH,
                                                          '/html/body/div[2]/div[2]/div[1]/div/div/div[1]/div[1]/div').text

    to_date = context.driver.find_element(By.XPATH,
                                          '/html/body/div[2]/div[2]/div[1]/div/div/div[2]/div/div[2]/div/div[1]/button[1]')
    to_date.click()
    time.sleep(2)

    to_date = context.driver.find_element(By.XPATH,
                                          '/html/body/div/div/main/div/div/div[2]/div/div[1]/div/div[2]/div/div[2]/div/div/div/div[2]/div[1]')
    to_date.click()
    time.sleep(2)

    back_next_button_to_date = context.driver.find_element(By.XPATH,
                                                           '/html/body/div[2]/div[2]/div[1]/div/div/div[1]/div[2]/button[1]')
    to_year_to_be_selected = context.driver.find_element(By.XPATH,
                                                         '/html/body/div[2]/div[2]/div[1]/div/div/div[1]/div[1]/div').text
    while to_year_to_be_selected != 'October 2023':
        back_next_button_to_date.click()
        to_year_to_be_selected = context.driver.find_element(By.XPATH,
                                                             '/html/body/div[2]/div[2]/div[1]/div/div/div[1]/div[1]/div').text
    time.sleep(1)
    context.driver.find_element(By.XPATH,
                                '/html/body/div[2]/div[2]/div[1]/div/div/div[2]/div/div[2]/div/div[1]/button[1]').click()
    time.sleep(2)

    element = context.driver.find_element(By.XPATH,
                                          "/html/body/div/div/main/div/div/div[2]/div/div[1]/div/div[2]/div/div[1]/div/div/svg/g[1]/g[3]/g[1]/path[1]").text
    print(element)
