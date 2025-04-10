import json
import pickle
import time
from errno import EAUTH

import allure
from allure_commons.types import AttachmentType
from mailosaur import MailosaurClient
from mailosaur.models import SearchCriteria
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from behave import *



chrome_options = Options()
chrome_options.add_argument("--incognito")
driver_path = "/Users/jerry/Desktop/QA-Automation/WHOZIN/driver/chrome-mac-arm64/chromedriver"


@allure.severity(allure.severity_level.CRITICAL)
@Given(u'User opens Konsuld URL with cookies-lc')
def step_impl(context):

    global auth_token, cookies
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get("https://dev.konsuld.app/")
    time.sleep(3)
    allure.attach(context.driver.get_screenshot_as_png(), name="testLoginScreen",
                  attachment_type=AttachmentType.PNG)



    login_button = context.driver.find_element(By.XPATH, "/html/body/div/div[1]/main/div/div/div/div/div/div/button[1]")
    login_button.click()
    time.sleep(2)
    allure.attach(context.driver.get_screenshot_as_png(), name="testMessageInAccount",
                  attachment_type=AttachmentType.PNG)



    email_field = context.driver.find_element(By.ID, 'email')
    email_field.send_keys('experiment-motion@fxxsta43.mailosaur.net')
    password_field = context.driver.find_element(By.ID, "password")
    password_field.send_keys('Admin@123')
    allure.attach(context.driver.get_screenshot_as_png(), name="testMessageInAccount",
                  attachment_type=AttachmentType.PNG)



    sign_in_button = context.driver.find_element(By.XPATH,
                                                 '//*[@id="root"]/div[1]/main/div/div[2]/div[1]/form/div/div/button')
    sign_in_button.click()
    allure.attach(context.driver.get_screenshot_as_png(), name="testMessageInAccount",
                  attachment_type=AttachmentType.PNG)
    time.sleep(8)



    api_key = "qQPQaRofMFcIgpMCqyIFBnd1nGT7oToq"
    server_id = "fxxsta43"
    server_domain = "fxxsta43.mailosaur.net"

    mailosaur = MailosaurClient(api_key)
    criteria = SearchCriteria()
    criteria.sent_to = "experiment-motion@" + server_domain

    # Get the email
    email = mailosaur.messages.get(server_id, criteria)
    print("Subject: " + email.subject)
    message = mailosaur.messages.get(server_id, criteria)

    # Get the first verification code
    first_code = message.html.codes[0]
    print(first_code.value)  # Prints the verification code, e.g., "456812"

    # Store the verification code in context for use in other steps
    context.verification_code = first_code.value



    # Retrieve the verification code from context
    verification_code = context.verification_code

    # Find the verification code input field and enter the code
    verification_code_field = context.driver.find_element(By.XPATH,
                                                          "//input[starts-with(@id, 'verification_code')]")
    verification_code_field.send_keys(verification_code)
    time.sleep(2)
    allure.attach(context.driver.get_screenshot_as_png(), name="testMessageInAccount",
                  attachment_type=AttachmentType.PNG)



    confirm_button = context.driver.find_element(By.XPATH,
                                                 "/html/body/div[1]/div[1]/main/div/div[2]/div/div/div/form/div/button")
    confirm_button.click()

    time.sleep(5)

    close_tutorial_button = context.driver.find_element(By.XPATH, "//button[contains(@aria-label, 'close')]")
    close_tutorial_button.click()
    time.sleep(1)
    allure.attach(context.driver.get_screenshot_as_png(), name="testMessageInAccount",
                  attachment_type=AttachmentType.PNG)

    time.sleep(5)
    try:
        auth_token = context.driver.execute_script("""
            return window.localStorage.getItem('access_token');
            """)

        referesh_token = context.driver.execute_script("""
                    return window.localStorage.getItem('refresh_token');
                """)

        print(f"Auth Token: {auth_token}")
        print(f"Auth Token: {referesh_token}")

    except Exception as e:
        time.sleep(3)

    pickle.dump(auth_token, open("../test-cases/oliver.pkl","wb"))



