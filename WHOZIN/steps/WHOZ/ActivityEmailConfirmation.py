import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from behave import *
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import random
import string
import time


chrome_options = Options()
chrome_options.add_argument("--incognito")
driver_path = "../../driver/chrome-mac-arm64/Google Chrome for Testing.app"




def generate_random_string(length=100):
    letters = string.ascii_letters  # Generates a string of all letters (both lowercase and uppercase)
    return ''.join(random.choice(letters) for _ in range(length))


@Given(u'The browser is launched')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    time.sleep(1)


@when(u'Whoz App is opened')
def step_impl(context):
    context.driver.get("https://uat.app.whoz.co")
    time.sleep(6)
    status = context.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/header/div/div/div[1]').is_displayed()

    if status == True:
        allure.attach(context.driver.get_screenshot_as_png(), name="testLoginScreen",
                      attachment_type=AttachmentType.PNG)
        assert True
    else:
        assert False


@when(u'User login the Whoz app')
def step_impl(context):
    email_field = context.driver.find_element(By.ID, 'email')
    email_field.send_keys('nahmed@technologyrivers.com')

    pass_field = context.driver.find_element(By.ID, 'password')
    pass_field.send_keys('Admin@123')
    time.sleep(2)

    login_button = context.driver.find_element(By.XPATH,
                                               '/html/body/div[1]/div[2]/div/main/div[2]/div/div/div/div/div[1]/form/div[7]/button')
    login_button.click()
    time.sleep(6)

    allure.attach(context.driver.get_screenshot_as_png(), name="testLoginScreen",
                  attachment_type=AttachmentType.PNG)


@when(u'Creates Activity successfully')
def step_impl(context):
    create_activity_button = context.driver.find_element(By.XPATH,
                                                         '//*[@id="navbar"]/div/div/div[2]/button[1]')
    create_activity_button.click()
    time.sleep(2)

    time.sleep(2)
    ActivityText = context.driver.find_element(By.XPATH,
                                               '/html/body/div[1]/div[2]/div/div/div[2]/div/div[2]/div/div/div[1]/p').text
    if ActivityText == "Let’s see":
        print("Navigated to activity screen successfully")
    else:
        print("Unable to navigate to activity page")

    file_input = context.driver.find_element(By.XPATH,
                                             "/html/body/div[1]/div[2]/div/div/div[2]/div/div[1]/div/div[3]/div/div/div/button")

    # Send the file path to the file input element
    file_input.send_keys('/html/body/div[2]/div/main/div[6]/div[1]/div/div[2]/div[1]/article/a/img')

    time.sleep(3)
    random_activity_name = generate_random_string(50)  # You can change the length as needed

    # Locate the activity title input field
    activity_title_input = context.driver.find_element(By.XPATH,
                                                       '/html/body/div[1]/div[2]/div/div/div[2]/div/div[2]/div/div/div[3]/div/div[2]/div/input')

    # Clear the input field if needed (optional)
    activity_title_input.clear()

    # Send the random activity name to the input field
    activity_title_input.send_keys(random_activity_name)
    time.sleep(2)

    activity_description = context.driver.find_element(By.XPATH,
                                                       '/html/body/div[1]/div[2]/div/div/div[2]/div/div[2]/div/div/div[3]/div/div[3]/div/div/textarea[1]')
    activity_description.send_keys(random_activity_name)

    time.sleep(2)

    max_guet = context.driver.find_element(By.XPATH,
                                           '/html/body/div[1]/div[2]/div/div/div[2]/div/div[2]/div/div/div[3]/div/div[4]/div/input')
    max_guet.send_keys('5')
    time.sleep(3)

    click_next_button = context.driver.find_element(By.XPATH,
                                                    '/html/body/div[1]/div[2]/div/div/div[2]/div/div[2]/div/div/div[3]/div/div[6]/button[2]')
    click_next_button.click()
    time.sleep(3)

    context.driver.execute_script("window.scrollTo(0, 0);")
    time.sleep(2)

    date_dropdown_xpath = '/html/body/div[1]/div[2]/div/div/div[2]/div/div[2]/div/div/div[3]/div/div[1]/div[2]/div/div/div[1]/div/div/div'
    date_dropdown = context.driver.find_element(By.XPATH, date_dropdown_xpath)
    date_dropdown.click()
    time.sleep(4)

    click_next_button_date_dropdown = context.driver.find_element(By.XPATH,
                                                                  '/html/body/div[3]/div[2]/div/div/div/div[1]/div[2]/button[2]')
    click_next_button_date_dropdown.click()
    time.sleep(5)

    # Now click the element
    select_activity_date_from_dropdown = context.driver.find_element(By.XPATH,
                                                                     "/html/body/div[3]/div[2]/div/div/div/div[2]/div/div/div[2]/div/div[3]/button[3]")
    select_activity_date_from_dropdown.click()

    time.sleep(3)

    start_date_menu = context.driver.find_element(By.XPATH,
                                                  '/html/body/div[1]/div[2]/div/div/div[2]/div/div[2]/div/div/div[3]/div/div[1]/div[2]/div/div/div[2]/div/div/div/button')
    start_date_menu.click()
    time.sleep(2)

    select_start_date = context.driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/div/div[1]/div/ul[1]/li[2]')
    select_start_date.click()
    time.sleep(3)

    end_date_menu = context.driver.find_element(By.XPATH,
                                                '//*[@id="root"]/div[2]/div/div/div[2]/div/div[2]/div/div/div[3]/div/div[1]/div[2]/div/div/div[3]/div/div/div/button')
    end_date_menu.click()
    time.sleep(3)

    select_end_time = context.driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/div/div[1]/div/ul[1]/li[3]')
    select_end_time.click()
    time.sleep(1)

    ok_button = context.driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/div/div[2]/button[2]')
    ok_button.click()
    time.sleep(2)

    context.driver.execute_script("window.scrollTo(0, 500);")
    time.sleep(2)

    location_field = context.driver.find_element(By.XPATH,
                                                 '/html/body/div[1]/div[2]/div/div/div[2]/div/div[2]/div/div/div[3]/div/div[3]/div[2]/div[2]/div/div/div/input')
    location_field.send_keys('office')
    time.sleep(5)

    google_fetched_location = context.driver.find_element(By.XPATH, '//*[@id="google-map-demo-option-0"]')
    google_fetched_location.click()
    time.sleep(5)

    next_button_second_screen = context.driver.find_element(By.XPATH,
                                                            '//*[@id="root"]/div[2]/div/div/div[2]/div/div[2]/div/div/div[3]/div/div[5]/button[2]')
    next_button_second_screen.click()
    time.sleep(2)

    context.driver.execute_script("window.scrollTo(0, 0);")
    time.sleep(2)

    brows_contact_button = context.driver.find_element(By.XPATH,
                                                       '//*[@id="root"]/div[2]/div/div/div[2]/div/div[2]/div/div/div[3]/div/div[2]/button')
    brows_contact_button.click()
    time.sleep(2)

    expand_all_contacts = context.driver.find_element(By.XPATH, '//*[@id="panel1a-header"]/div[2]')
    expand_all_contacts.click()
    time.sleep(6)

    contacts_checkbox = context.driver.find_element(By.XPATH,
                                                    '//*[@id="panel1a-content"]/div/div/div[1]/div/div[2]/div[1]/div/div/div[1]/div[1]/div/div/span/input')
    contacts_checkbox.click()
    time.sleep(2)

    done_button_contacts = context.driver.find_element(By.XPATH,
                                                       '//*[@id="root"]/div[2]/div/div/div[2]/div/div[1]/div[2]/button')
    done_button_contacts.click()
    time.sleep(2)

    context.driver.execute_script("window.scrollTo(0, 500);")
    time.sleep(2)

    next_button_third_screen = context.driver.find_element(By.XPATH,
                                                           '//*[@id="root"]/div[2]/div/div/div[2]/div/div[2]/div/div/div[3]/div/div[6]/button[2]')
    next_button_third_screen.click()
    time.sleep(2)

    send_invites_button = context.driver.find_element(By.XPATH,
                                                      '//*[@id="root"]/div[2]/div/div/div[2]/div/div[2]/div/div/div[3]/div/div[3]/button[2]')
    send_invites_button.click()
    time.sleep(2)
    allure.attach(context.driver.get_screenshot_as_png(), name="testLoginScreen",
                  attachment_type=AttachmentType.PNG)


@then(u'Navigates to the view activity screen')
def step_impl(context):
    context.driver.execute_script("window.scrollTo(0, 500);")
    time.sleep(2)

    view_activity_button = context.driver.find_element(By.XPATH, '/html/body/div[3]/div[3]/div/div/div[3]/button')
    view_activity_button.click()
    time.sleep(2)
    allure.attach(context.driver.get_screenshot_as_png(), name="testLoginScreen",
                  attachment_type=AttachmentType.PNG)
    context.driver.close()



@given(u'Open the mailtrap')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get("https://mailtrap.io/")
    time.sleep(6)
    allure.attach(context.driver.get_screenshot_as_png(), name="testLoginScreen",
                  attachment_type=AttachmentType.PNG)



@when(u'Login into the mailtrap')
def step_impl(context):

    mailtrap_signin_button = context.driver.find_element(By.XPATH,'/html/body/div[1]/header/nav/div/div/div[2]/div[4]/a[1]')
    mailtrap_signin_button.click()
    time.sleep(3)

    mailtrap_email = context.driver.find_element(By.XPATH,'/html/body/main/div/div[1]/form/div[1]/input')
    mailtrap_email.send_keys('engr.sana.shah@gmail.com')

    mailtrap_next = context.driver.find_element(By.XPATH,'/html/body/main/div/div[1]/form/div[3]/a')
    mailtrap_next.click()
    time.sleep(3)

    mailtrap_password = context.driver.find_element(By.XPATH,'/html/body/main/div/div[1]/form/div[2]/div[1]/input')
    mailtrap_password.send_keys('Tr@123456')

    context.driver.execute_script("window.scrollTo(0, 500);")
    time.sleep(2)

    mail_trap_login_button = context.driver.find_element(By.XPATH,'//*[@id="new_user"]/div[2]/div[3]/input')
    mail_trap_login_button.click()
    time.sleep(5)
    allure.attach(context.driver.get_screenshot_as_png(), name="testLoginScreen",
                  attachment_type=AttachmentType.PNG)



@when(u'Navigate to Mailtrap Inbox')
def step_impl(context):
    mailtrap_inboxes = context.driver.find_element(By.LINK_TEXT, "Inboxes →")
    mailtrap_inboxes.click()
    time.sleep(1)

    mailtrap_whoz_inbox = context.driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/div[2]/div/div[2]/div/div[3]/div/div[1]/span/a/span')
    mailtrap_whoz_inbox.click()
    time.sleep(1)
    allure.attach(context.driver.get_screenshot_as_png(), name="testLoginScreen",
                  attachment_type=AttachmentType.PNG)

@then(u'Verify activity email is sent to the users')
def step_impl(context):
    pass



