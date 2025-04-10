from selenium import webdriver
import time

from behave import *
from selenium.webdriver.common.by import By
import logging
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver_path = "../driver/chrome-mac-arm64/Google Chrome for Testing.app/Contents/MacOS/Google Chrome for Testing"


@given('launched chrome browser2')
def UserIsOnLoginPage(context):
    try:
        print('Launching browser')
        context.driver = webdriver.Chrome()
        context.driver.maximize_window()
    except Exception as e:
        print("Error:", e)


@When('User navigates to the login page2')
def UserIsOnLoginPage(context):
    try:
        context.driver.get("https://qa.portal.admin.scanmygolfball.com/login")
        time.sleep(3)
    except Exception as e:
        print("Error:", e)


@when('Enter username2 "{user2}" and password2 "{pwd2}"')
def EnterCreds(context, user2, pwd2):
    context.driver.find_element(By.ID, "outlined-adornment-email-login").send_keys(user2)
    context.driver.find_element(By.ID, "outlined-adornment-password-login").send_keys(pwd2)
    logging.debug('This is a debug message')
    time.sleep(3)


@when(u'Click on Login button2')
def step_impl(context):
    context.driver.find_element(By.XPATH,
                                '//*[@id="root"]/div/div/div/div[1]/div/div/div/div/div/div[3]/form/div[3]/div/button').click()
    time.sleep(2)


@given(u'User is on the Admin Dashboard2')
def step_impl(context):
    try:
        dashboard = context.driver.find_element(By.XPATH,
                                                '/html/body/div/div/nav/div/div/div[2]/ul/a[1]/div[2]/h5').text

    except:
        context.driver.close()
        assert False, 'Testcase Failed'

    if dashboard == "Dashboard":
        assert True, "Testcase Passed"


@when(u'User navigates to the Summary section2')
def step_impl(context):
    time.sleep(5)

    summary_section = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "/html/body/div/div/main/div/div/div[1]/div/div/div/div[2]/div/div/div[1]/div/div"))
    ).text

    time.sleep(2)

    if summary_section == 'Summary':
        print("Successfully navigated to the Summary Section")
    else:
        print("Failed to navigate to Summary section")


@then(u'check that the registered user section is working fine')
def step_impl(context):
    try:
        registered_users_dashboard_no = context.driver.find_element(By.XPATH,
                                                                    '/html/body/div/div/main/div/div/div[1]/div/div/div/div[2]/div/div/div[2]/div/div/h3').text
        time.sleep(3)

        registered_users_section = context.driver.find_element(By.XPATH,
                                                               '/html/body/div/div/main/div/div/div[1]/div/div/div/div[2]/div/div/div[2]/div/div/h3')
        registered_users_section.click()
        time.sleep(2)

        registered_users_section_active_users_no = int(
            context.driver.find_element(By.XPATH, '/html/body/div/div/main/div/div[3]/div/p[2]').text)
        time.sleep(2)

        if registered_users_section_active_users_no == registered_users_dashboard_no and context.driver.find_element(
                By.XPATH, '/html/body/div/div/main/div/div[1]/div/div[3]/div/div').text == 'Registered':
            print('Registered Users count test case passed')
        else:
            print('Registered Users count test case Failed')

        time.sleep(2)

    except Exception as e:
        print("Error:", e)


@then(u'check that the guest user section is working fine')
def step_impl(context):
    time.sleep(2)
    context.driver.find_element(By.XPATH, '/html/body/div/div/nav/div/div/div[2]/ul/a[1]').click()
    time.sleep(2)
    try:
        time.sleep(3)
        guest_users_dashboard_no = int(context.driver.find_element(By.XPATH,
                                                                   '/html/body/div/div/main/div/div/div[1]/div/div/div/div[2]/div/div/div[3]/div/div/h3').text)
        print(guest_users_dashboard_no)
        time.sleep(3)

        guest_users_section = context.driver.find_element(By.XPATH,
                                                          '/html/body/div/div/main/div/div/div[1]/div/div/div/div[2]/div/div/div[3]/div/div/h6')
        guest_users_section.click()
        time.sleep(2)

        guest_users_section_active_users_no = context.driver.find_element(By.XPATH,
                                                                          '/html/body/div/div/main/div/div[3]/div/p[2]').text
        time.sleep(2)
        count_text = guest_users_section_active_users_no.split('of')[1].strip()
        print(count_text)
        time.sleep(2)

        user_type = context.driver.find_element(By.XPATH, '/html/body/div/div/main/div/div[1]/div/div[3]/div/div').text
        print(user_type)

        if int(count_text) == guest_users_dashboard_no and user_type == "Guests":
            print('GUEST USERS COUNT PASSED')
        else:
            print('GUEST USERS COUNT FAILED')

        time.sleep(2)

    except Exception as e:
        print("Error:", e)


@then(u'check that the Balls section is working fine')
def step_impl(context):
    try:

        time.sleep(2)
        WebDriverWait(context.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/nav/div/div/div[2]/ul/a[1]'))).click()
        ball_no_appearing_on_dashboard = context.driver.find_element(By.XPATH,
                                                                     '/html/body/div/div/main/div/div/div[1]/div/div/div/div[2]/div/div/div[4]/div/div/h3').text
        time.sleep(3)
        context.driver.find_element(By.XPATH,
                                    '/html/body/div/div/main/div/div/div[1]/div/div/div/div[2]/div/div/div[4]/div/div/h3').click()
        time.sleep(2)
        ball_no_appearing_on_ball_listing = context.driver.find_element(By.XPATH,
                                                                        '/html/body/div/div/main/div/div/div[3]/div/p[2]').text
        ball_no_appearing_on_ball_listing1 = ball_no_appearing_on_ball_listing.split('of')[1].strip()

        if int(ball_no_appearing_on_dashboard) == int(ball_no_appearing_on_ball_listing1):
            print(
                "Golf ball count test case passed:\n" + ball_no_appearing_on_ball_listing1 + "\n" + ball_no_appearing_on_dashboard)
        else:
            print(
                "Golf ball count test case failed:\n" + ball_no_appearing_on_ball_listing1 + "\n" + ball_no_appearing_on_dashboard)
    except Exception as e:
        print("Error:", e)


@then(u'check that the Scanner count is visible')
def step_impl(context):
    WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/nav/div/div/div[2]/ul/a[1]'))).click()

    scanner_count = context.driver.find_element(By.XPATH,
                                                '/html/body/div/div/main/div/div/div[1]/div/div/div/div[2]/div/div/div[5]/div/div/h6').text
    if scanner_count == 'Scanner Count':
        print("The scanner count is visible")
    else:
        print("The scanner count is not visible")


@then(u'check that the Scan Results section is working fine')
def step_impl(context):
    try:
        scan_results = context.driver.find_element(By.XPATH,
                                                   '/html/body/div/div/main/div/div/div[1]/div/div/div/div[2]/div/div/div[6]/div/div/h3').text
        time.sleep(3)
        context.driver.find_element(By.XPATH,
                                    '/html/body/div/div/main/div/div/div[1]/div/div/div/div[2]/div/div/div[6]/div/div/h3').click()

        time.sleep(3)
        scanning_mode_no1 = context.driver.find_element(By.XPATH,
                                                        '/html/body/div/div/main/div/div[2]/div[3]/div/p[2]').text
        scanning_mode_no = scanning_mode_no1.split('of')[1].strip()

        time.sleep(3)
        WebDriverWait(context.driver,10).until(
            EC.element_to_be_clickable((By.XPATH,'/html/body/div/div/main/div/div[2]/div[1]/div/div/div[2]/div/a[2]'))).click()

        time.sleep(2)
        manual_mode1 = context.driver.find_element(By.XPATH, '/html/body/div/div/main/div/div[2]/div[3]/div/p[2]').text
        manual_mode_no = manual_mode1.split('of')[1].strip()

        print('scanning mode', scanning_mode_no)
        print('manual mode', manual_mode_no)
        print('scam results no ', scan_results)

        a = int(scanning_mode_no) + int(manual_mode_no)
        print('The sum is', a)

        if int(scanning_mode_no) + int(manual_mode_no) == int(scan_results):
            print('Scan Result count test case passed')
        else:
            print("scan result test case failed")
    except Exception as e:
        print("Error", e)
