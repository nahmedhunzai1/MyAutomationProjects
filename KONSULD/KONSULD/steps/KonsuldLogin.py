from selenium.webdriver.support import expected_conditions as EC
from mailosaur import MailosaurClient
from mailosaur.models import SearchCriteria
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
import allure
from allure_commons.types import AttachmentType
from behave import *
import time

chrome_options = Options()
chrome_options.add_argument("--incognito")
driver_path = "/Users/jerry/Desktop/QA-Automation/WHOZIN/driver/chrome-mac-arm64/chromedriver"

@allure.severity(allure.severity_level.CRITICAL)
@Given(u'User opens Konsuld URL-1')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get("https://dev.konsuld.app/")
    time.sleep(3)
    allure.attach(context.driver.get_screenshot_as_png(), name="testLoginScreen",
                  attachment_type=AttachmentType.PNG)
    time.sleep(1)
    allure.attach(context.driver.get_screenshot_as_png(), name="testMessageInAccount",
                  attachment_type=AttachmentType.PNG)

@when(u'click Log In button-1')
def step_impl(context):
    login_button = context.driver.find_element(By.XPATH, "/html/body/div/div[1]/main/div/div/div/div/div/div/button[1]")
    login_button.click()
    time.sleep(2)
    allure.attach(context.driver.get_screenshot_as_png(), name="testMessageInAccount",
                  attachment_type=AttachmentType.PNG)

@when(u'enter email and password-1')
def step_impl(context):
    email_field = context.driver.find_element(By.ID, 'email')
    email_field.send_keys('nahmed@ohkfhtut.mailosaur.net')
    password_field = context.driver.find_element(By.ID, "password")
    password_field.send_keys('Admin@123')
    allure.attach(context.driver.get_screenshot_as_png(), name="testMessageInAccount",
                  attachment_type=AttachmentType.PNG)

@when(u'click Sign In button-1')
def step_impl(context):
    sign_in_button = context.driver.find_element(By.XPATH,
                                                 '//*[@id="root"]/div[1]/main/div/div[2]/div[1]/form/div/div/button')
    sign_in_button.click()
    allure.attach(context.driver.get_screenshot_as_png(), name="testMessageInAccount",
                  attachment_type=AttachmentType.PNG)
    time.sleep(8)


@when(u'Get the verfication code from mailosaurs inbox-1')
def step_impl(context):
    api_key = "sTGHyYSV6ZIgFf0NEro9QJuuNu7klmWr"
    server_id = "ohkfhtut"
    server_domain = "ohkfhtut.mailosaur.net"

    mailosaur = MailosaurClient(api_key)
    criteria = SearchCriteria()
    criteria.sent_to = "nahmed@" + server_domain

    # Get the email
    email = mailosaur.messages.get(server_id, criteria)
    print("Subject: " + email.subject)
    message = mailosaur.messages.get(server_id, criteria)

    # Get the first verification code
    first_code = message.html.codes[0]
    print(first_code.value)  # Prints the verification code, e.g., "456812"

    # Store the verification code in context for use in other steps
    context.verification_code = first_code.value


@when(u'enter it in the verification code section-1')
def step_impl(context):
        # Retrieve the verification code from context
        verification_code = context.verification_code

        # Find the verification code input field and enter the code
        verification_code_field = context.driver.find_element(By.XPATH,
                                                              "//input[starts-with(@id, 'verification_code')]")
        verification_code_field.send_keys(verification_code)
        time.sleep(2)
        allure.attach(context.driver.get_screenshot_as_png(), name="testMessageInAccount",
                      attachment_type=AttachmentType.PNG)




@when(u'click confirm-1')
def step_impl(context):
    confirm_button = context.driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/main/div/div[2]/div/div/div/form/div/button")
    confirm_button.click()

    time.sleep(5)
    allure.attach(context.driver.get_screenshot_as_png(), name="testMessageInAccount",
                  attachment_type=AttachmentType.PNG)




@then(u'user must login the app-1')
def step_impl(context):
    try:
        # Wait until the element containing "Home" is visible
        home_konsuld_element = WebDriverWait(context.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH,
                                              "/html/body/div[1]/div[1]/main/div/div[2]/div/div[1]/div/div[1]/div/div[2]/ul/li[1]/div[2]/span"))
        )

        # Retrieve the text of the element
        home_konsuld = home_konsuld_element.text

        # Check if the text is "Home"
        if home_konsuld == "Home":
            print("Successfully logged in")
        else:
            print("Test failed: Expected 'Home', but got:", home_konsuld)
    except Exception as e:
        print("Test failed due to an exception:", str(e))