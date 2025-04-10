from selenium import webdriver
import time

from behave import *
from selenium.webdriver.common.by import By
import logging
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver_path = "../driver/chrome-mac-arm64/Google Chrome for Testing.app/Contents/MacOS/Google Chrome for Testing"


@given('launched chrome browser')
def UserIsOnLoginPage(context):
    print('Launching browser')
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()


@When('User navigates to the login page')
def UserIsOnLoginPage(context):
    context.driver.get("https://qa.portal.admin.scanmygolfball.com/login")
    time.sleep(3)


@when('Enter username1 "{user1}" and password1 "{pwd1}"')
def EnterCreds(context, user1, pwd1):
    context.driver.find_element(By.ID, "outlined-adornment-email-login").send_keys(user1)
    context.driver.find_element(By.ID, "outlined-adornment-password-login").send_keys(pwd1)
    logging.debug('This is a debug message')
    time.sleep(3)


@when(u'Click on Login button1')
def step_impl(context):
    context.driver.find_element(By.XPATH,
                                '//*[@id="root"]/div/div/div/div[1]/div/div/div/div/div/div[3]/form/div[3]/div/button').click()
    time.sleep(2)


@given(u'User is on the Admin Dashboard')
def step_impl(context):
    try:
        dashboard = context.driver.find_element(By.XPATH,
                                                '/html/body/div/div/nav/div/div/div[2]/ul/a[1]/div[2]/h5').text

    except:
        context.driver.close()
        assert False, 'Testcase Failed'

    if dashboard == "Dashboard":
        assert True, "Testcase Passed"


@when(u'User navigates to the Active User section')
def step_impl(context):
    time.sleep(5)
    active_users_element = context.driver.find_element(By.XPATH, "/html/body/div/div/main/div/div/div["
                                                                 "1]/div/div/div/div["
                                                                 "1]/div/div/div[1]/div/div/p").text
    time.sleep(2)

    if active_users_element == 'Active Users':
        print("Successfully navigated to the Active Users Section")
    else:
        print("Failed to navigate to active users section")

    time.sleep(2)


@when(u'User must observe that active users is appearing correct')
def step_impl(context):
    global listing_count
    try:
        context.driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/div[1]/div/div/div/div[1]/div/div/div['
                                              '2]/div/div/h6').click()  # click on total active users
        time.sleep(2)
        listing_table = context.driver.find_element(By.XPATH,
                                                    "/html/body/div[2]/div[3]/div[2]/table/tbody")  # Modify with your actual element
        time.sleep(2)
        listing_rows = listing_table.find_elements(By.TAG_NAME, "tr")
        listing_count = len(listing_rows)
        print(f"Total listings in the Admin Panel: {listing_count}")

        time.sleep(3)

    except Exception as e:
        print("Error:", e)

    total_active_users_shown = context.driver.find_element(By.XPATH, "/html/body/div/div/main/div/div/div["
                                                                     "1]/div/div/div/div[1]/div/div/div["
                                                                     "2]/div/div/h3").text  # --> Fetching the active
    print("The total active users shown", total_active_users_shown)
    # users number as it is shown in admin panel dashboard
    active_users = int(total_active_users_shown)
    print(type(listing_count))
    print(type(active_users))
    if listing_count == active_users:
        print('passed')
    else:
        print('The listing count is not equal to listing row numbers therefore test case is failed')
    time.sleep(3)
    context.driver.find_element(By.XPATH, "/html/body/div[2]/div[3]/div[1]/div/button").click()
    time.sleep(2)


@when(u'User must observe that the Past 24 Hours Users are appearing Correct')
def step_impl(context):
    try:

        past_24_hr = context.driver.find_element(By.XPATH,
                                                 "/html/body/div/div/main/div/div/div[1]/div/div/div/div["
                                                 "1]/div/div/div["
                                                 "3]/div/div/h3").text  # --> saving text of past 24 hours
        time.sleep(2)
        past_24_hours_users = int(past_24_hr)
        print(type(past_24_hours_users))
        time.sleep(2)
        context.driver.find_element(By.XPATH,
                                    "/html/body/div/div/main/div/div/div[1]/div/div/div/div[1]/div/div/div["
                                    "3]/div/div/h3").click()  # --> clicking past 24 hours option
        time.sleep(3)

        listing_table_24 = WebDriverWait(context.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[3]/div[2]/table/tbody")
                                       ))

        time.sleep(2)
        listing_rows_24 = listing_table_24.find_elements(By.TAG_NAME, "tr")
        listing_count_24 = len(listing_rows_24)
        print(f"Total listings in the Admin Panel: {listing_count_24}")

        if past_24_hours_users == listing_count_24:
            time.sleep(2)
            print('Last 24 hours count testing passed')

        else:
            time.sleep(2)
            print('last 24 hours testing count failed')

        print(past_24_hours_users)
        print(listing_count_24)

        time.sleep(5)
        context.driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div[1]/div/button').click()
        time.sleep(2)
    except Exception as e:
        print(f"No active users found for last 24 hours : {e}")


@when(u'User must observe that the Past 7 days Users are appearing Correct')
def step_impl(context):
    past_7 = context.driver.find_element(By.XPATH,
                                         "/html/body/div/div/main/div/div/div[1]/div/div/div/div[1]/div/div/div["
                                         "4]/div/div/h3").text  # --> saving text of past 7
    # days
    time.sleep(2)
    past_7_days = int(past_7)
    print(type(past_7_days))
    time.sleep(2)
    context.driver.find_element(By.XPATH,
                                "/html/body/div/div/main/div/div/div[1]/div/div/div/div[1]/div/div/div["
                                "4]/div/div/h3").click()  # --> clicking past 7 days option
    time.sleep(2)
    listing_table_7_days = context.driver.find_element(By.XPATH,
                                                       "/html/body/div[2]/div[3]/div[2]/table/tbody")  # --> Counting row

    # numbers
    time.sleep(2)
    listing_rows_7_days = listing_table_7_days.find_elements(By.TAG_NAME, "tr")
    listing_rows_7_days = len(listing_rows_7_days)
    print(f"Total listings in the Admin Panel: {listing_rows_7_days}")

    if past_7_days == listing_rows_7_days:
        time.sleep(2)
        print('Last 7 days count testing passed')

    else:
        time.sleep(2)
        print('last 7 days testing count failed')

    print(past_7_days)
    print(listing_rows_7_days)

    time.sleep(5)
    context.driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div[1]/div/button').click()
    time.sleep(2)


@when(u'User must observe that the Past 30 days Users are appearing Correct')
def step_impl(context):
    past_30 = context.driver.find_element(By.XPATH,
                                          "/html/body/div/div/main/div/div/div[1]/div/div/div/div[1]/div/div/div["
                                          "5]/div/div/h3").text  # --> saving text of past 30
    # days
    time.sleep(2)
    past_30_days = int(past_30)
    print(type(past_30_days))
    time.sleep(2)
    context.driver.find_element(By.XPATH,
                                "/html/body/div/div/main/div/div/div[1]/div/div/div/div[1]/div/div/div["
                                "5]/div/div/h3").click()  # --> clicking past 7 days option
    time.sleep(2)
    listing_table_30_days = context.driver.find_element(By.XPATH,
                                                        "/html/body/div[2]/div[3]/div[2]/table/tbody")  # --> Counting row

    # numbers
    time.sleep(2)
    listing_rows_30_days = listing_table_30_days.find_elements(By.TAG_NAME, "tr")
    listing_rows_30_days = len(listing_rows_30_days)
    print(f"Total listings in the Admin Panel: {listing_rows_30_days}")

    if past_30_days == listing_rows_30_days:
        time.sleep(2)
        print('Last 30 days count testing passed')

    else:
        time.sleep(2)
        print('last 30 days testing count failed')

    print(past_30_days)
    print(listing_rows_30_days)

    time.sleep(5)
    context.driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div[1]/div/button').click()
    time.sleep(2)


@when(u'Verify the Active Users Date filter is working')
def step_impl(context):
    from_date_filter = context.driver.find_element(By.XPATH,
                                                   '/html/body/div/div/main/div/div/div[1]/div/div/div/div['
                                                   '1]/div/div/div['
                                                   '2]/div/div/div/div[1]/div[1]')
    from_date_filter.click()
    time.sleep(2)

    next_button = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[2]/div[1]/div/div/div[1]/div[2]/button[1]"))
    )
    time.sleep(5)

    required_year = context.driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[1]/div/div/div[1]/div[1]/div')
    time.sleep(2)

    while required_year.text != 'June 2023':
        next_button.click()
    time.sleep(2)

    from_date = context.driver.find_element(By.XPATH,
                                            '/html/body/div[2]/div[2]/div[1]/div/div/div[2]/div/div[2]/div/div['
                                            '2]/button[3]')
    from_date.click()
    time.sleep(2)

    to_date_filter = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/main/div/div/div[1]/div/div/div/div[1]/div/div/div["
                                              "2]/div/div/div/div[2]/div[1]"))
    )
    to_date_filter.click()

    back_button = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[2]/div[1]/div/div/div[1]/div[2]/button[1]"))
    )

    to_required_year = context.driver.find_element(By.XPATH,
                                                   '/html/body/div[2]/div[2]/div[1]/div/div/div[1]/div[1]/div')
    while to_required_year.text != 'October 2023':
        back_button.click()
        time.sleep(2)

    to_date = context.driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[1]/div/div/div[2]/div/div['
                                                    '2]/div/div[1]/button[1]')
    to_date.click()
    time.sleep(2)

    active_users_no = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div/div['
                                              '1]/div/div/div/div[1]/div/div/div['
                                              '2]/div/div/h3'))).text
    active_users_in_selected_date = int(active_users_no)

    time.sleep(3)

    if active_users_in_selected_date == 395:
        print('active users for the selected date is printed correct therefore testcase passed')
    else:
        print('The active users in the selected date is printed wrong and test case failed')

    time.sleep(4)
