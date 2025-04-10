import allure
from behave import *
from selenium.webdriver.chrome.options import Options
import random
import string
import time
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


chrome_options = Options()
chrome_options.add_argument("--incognito")
driver = webdriver.Chrome()

driver_path = "/Users/jerry/Desktop/QA-Automation/WHOZIN/driver/chrome-mac-arm64/chromedriver"




def generate_random_string(length=100):
    letters = string.ascii_letters  # Generates a string of all letters (both lowercase and uppercase)
    return ''.join(random.choice(letters) for _ in range(length))

def get_email ():
    random_number = random.randint(10,99999)
    email_random = f"nahmed+{str(random_number)}@technologyrivers.com";
    return email_random


@allure.severity(allure.severity_level.CRITICAL)
@When(u'User opens Konsuld URL-2')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get("https://dev.konsuld.app/")

    time.sleep(3)

    allure.attach(context.driver.get_screenshot_as_png(), name="testLoginScreen", attachment_type=AttachmentType.PNG)
    time.sleep(1)

@allure.severity(allure.severity_level.NORMAL)
@when(u'Click Sign up button-2')
def step_impl(context):

    context.driver.find_element(By.XPATH,"/html/body/div/div[1]/main/div/div/div/div/div/div/button[2]").click()
    context.driver.execute_script("window.scrollTo(0, 500);")
    time.sleep(2)

    # Sign_up = context.driver.find_element(By.XPATH,'/html/body/div/div[1]/main/div/div/div/div/div/form/div/button[2]')
    # Sign_up.click()

    allure.attach(context.driver.get_screenshot_as_png(), name="testsignup", attachment_type=AttachmentType.PNG)
    time.sleep(2)

@allure.severity(allure.severity_level.NORMAL)
@when(u'Fill the sign up form with valid email-2')
def step_impl(context):
    # prefix_select = context.driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/main/div/div[2]/div[1]/form/div/div[1]/div/div[3]/div/div[1]/div/div/div/div/input')
    # prefix_select.click()
    # time.sleep(3)

    gender_selection = context.driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/main/div/div[2]/div[1]/form/div/div[1]/div/div[2]/div/div[1]/div/div/div/div/input')
    gender_selection.send_keys('Mr.')
    time.sleep(2)

    first_name = context.driver.find_element(By.ID,'firstname')
    first_name.send_keys('Nadeem')

    last_name = context.driver.find_element(By.ID,"lastname")
    last_name.send_keys('Ahmed')

    email = context.driver.find_element(By.ID,'email')
    random_email = get_email()
    email.send_keys(random_email)

    allure.attach(context.driver.get_screenshot_as_png(), name="testSignupForm", attachment_type=AttachmentType.PNG)
    time.sleep(1)

@allure.severity(allure.severity_level.NORMAL)
@when(u'Acccept terms and conditions-2')
def step_impl(context):
    terms_and_conds = context.driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/main/div/div[2]/div[1]/form/div/div[1]/div/div[3]/label/span/input')
    terms_and_conds.click()

    membership_criteria = context.driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/main/div/div[2]/div[1]/form/div/div[1]/div/div[4]/label/span/input")
    membership_criteria.click()

    allure.attach(context.driver.get_screenshot_as_png(), name="testTermsandConditions", attachment_type=AttachmentType.PNG)
    time.sleep(1)

@allure.severity(allure.severity_level.CRITICAL)
@then(u'click create account button-2')
def step_impl(context):
    context.driver.execute_script("window.scrollTo(0, 500);")
    time.sleep(2)


    create_account_button = context.driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/main/div/div[2]/div[1]/form/div/div[2]/button')
    create_account_button.click()
    time.sleep(10)
    allure.attach(context.driver.get_screenshot_as_png(), name="testButton", attachment_type=AttachmentType.PNG)
    context.driver.close()


@allure.severity(allure.severity_level.CRITICAL)
@when(u'User opens gmail-2')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get("https://mail.google.com/mail/u/0/#inbox")
    time.sleep(3)
    allure.attach(context.driver.get_screenshot_as_png(), name="testLoginGmail", attachment_type=AttachmentType.PNG)


@allure.severity(allure.severity_level.CRITICAL)
@when(u'Login account-2')
def step_impl(context):
    google_email = context.driver.find_element(By.XPATH, '//*[@id="identifierId"]')
    google_email.send_keys("nahmed@technologyrivers.com")
    time.sleep(2)

    allure.attach(context.driver.get_screenshot_as_png(), name="testGoogleEmail", attachment_type=AttachmentType.PNG)


    click_next_button = context.driver.find_element(By.XPATH, '//*[@id="identifierNext"]/div/button/span')
    click_next_button.click()
    time.sleep(3)

    allure.attach(context.driver.get_screenshot_as_png(), name="testNextButton", attachment_type=AttachmentType.PNG)

    email_password = context.driver.find_element(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input')
    email_password.send_keys('Techrivers@123')
    time.sleep(2)

    allure.attach(context.driver.get_screenshot_as_png(), name="testEMail", attachment_type=AttachmentType.PNG)



    context.driver.find_element(By.XPATH, '//*[@id="passwordNext"]/div/button/span').click()
    time.sleep(5)

    allure.attach(context.driver.get_screenshot_as_png(), name="FinalScreen", attachment_type=AttachmentType.PNG)


    # click_continue_button = context.driver.find_element(By.XPATH,
    #                                                     '/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[3]/div/div/div[2]/div/div/button/span')
    # click_continue_button.click()
    # time.sleep(10)

@allure.severity(allure.severity_level.CRITICAL)
@when(u'Verify the message in the account-2')
def step_impl(context):
    inbox_email = context.driver.find_element(By.XPATH,'/html/body/div[7]/div[3]/div/div[2]/div[4]/div/div/div/div[2]/div/div[1]/div/div[1]/div[5]/div[1]/div/table/tbody/tr[1]/td[4]/div[2]/span[1]/span')
    inbox_email.click()
    time.sleep(2)

    allure.attach(context.driver.get_screenshot_as_png(), name="testMessageInAccount", attachment_type=AttachmentType.PNG)


    context.driver.execute_script("window.scrollTo(0, 1000);")
    time.sleep(2)
    # time_email = context.driver.find_element(By.XPATH,'/html/body/div[7]/div[3]/div/div[2]/div[4]/div/div/div/div[2]/div/div[1]/div/div[3]/div/div[2]/div[2]/div/div[3]/div[5]/div/div/div/div/div[1]/div[2]/div[1]/table/tbody/tr[1]/td[2]/div/span[2]')
    # if time_email.text == ''



@allure.severity(allure.severity_level.CRITICAL)
@when(u'redirected to the kunsuld webiste-2')
def step_impl(context):
    verification_link = context.driver.find_element(By.XPATH, "//p[strong[contains(text(), 'Verification Link')]]/strong/a")
    verification_link.click()
    # email_verification_url.click()
    time.sleep(15)

    original_window = context.driver.current_window_handle
    new_window = None

    for handle in context.driver.window_handles:
        if handle != original_window:
            new_window = handle
            break

    # Switch to the new window
    if new_window:
        context.driver.switch_to.window(new_window)

    allure.attach(context.driver.get_screenshot_as_png(), name="testFinalScreen", attachment_type=AttachmentType.PNG)

# @allure.severity(allure.severity_level.CRITICAL)
# @when(u'click lets get started button')
# def step_impl(context):
#     get_started_button = context.driver.find_element(By.XPATH,'/html/body')
#     get_started_button.click()
#     time.sleep(3)
#
#
# @allure.severity(allure.severity_level.CRITICAL)
# @when(u'Enter the NPI number and attachment ')
# def step_impl(context):




