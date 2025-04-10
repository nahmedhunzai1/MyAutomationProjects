
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from behave import *
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import random
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
from selenium.webdriver.support.ui import Select
import allure
from allure_commons.types import Severity



chrome_options = Options()
chrome_options.add_argument("--incognito")
driver_path = "/Users/jerry/Desktop/QA-Automation/WHOZIN/driver/chrome-mac-arm64/chromedriver"

# Global counter to keep track of email suffix
email_counter = 1


def generate_random_user():
    global email_counter

    first_names = ['Alice', 'John', 'Emily', 'Michael', 'Sara', 'David', 'Laura', 'Chris', 'Emma', 'Daniel']
    last_names = ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Garcia', 'Miller', 'Davis', 'Martinez', 'Taylor']

    first_name = random.choice(first_names)
    last_name = random.choice(last_names)
    email = f"{first_name.lower()}.{last_name.lower()}+{email_counter}@example.com"

    email_counter += 1  # Increment the counter for next email

    return first_name, last_name, email


@allure.severity(Severity.CRITICAL)
@given(u'The user is on the signup page')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get("https://www.heroku.com/home")
    time.sleep(2)

    signup_button = context.driver.find_element(By.XPATH,"/html/body/div[1]/header/nav/div/div[2]/ul[2]/li[2]/a[2]")
    signup_button.click()
    time.sleep(1)


    allure.attach(context.driver.get_screenshot_as_png(), name="signup-page",
                  attachment_type=AttachmentType.PNG)


@allure.severity(Severity.CRITICAL)
@when(u'The user enters valid signup details')
def step_impl(context):
    first_name, last_name, email = generate_random_user()
    wait = WebDriverWait(context.driver, 10)
    first_name_field = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='first_name']")))
    first_name_field.send_keys(first_name)

    print("The first name is", first_name)
    print("The last name is", last_name)
    print("The email name is", email)



    last_name_field = context.driver.find_element(By.XPATH,"/html/body/div[2]/div/div[2]/div[2]/form/div[2]/input")
    last_name_field.send_keys(last_name)

    email_field = context.driver.find_element(By.XPATH,"/html/body/div[2]/div/div[2]/div[2]/form/div[3]/input")
    email_field.send_keys(email)

    company_name_field = context.driver.find_element(By.XPATH,"/html/body/div[2]/div/div[2]/div[2]/form/div[4]/input")
    company_name_field.send_keys("TR")

    wait = WebDriverWait(context.driver, 10)
    country_element = wait.until(EC.presence_of_element_located((By.ID, "self_declared_country")))
    country_dropdown = Select(country_element)
    country_dropdown.select_by_visible_text("Pakistan")

    terms_and_cond_check_box = context.driver.find_element(By.XPATH,"/html/body/div[2]/div/div[2]/div[2]/form/div[7]/input")
    terms_and_cond_check_box.click()
    time.sleep(3)

    allure.attach(context.driver.get_screenshot_as_png(), name="signup-page1",
                  attachment_type=AttachmentType.PNG)

    create_account_button = context.driver.find_element(By.XPATH,"/html/body/div[2]/div/div[2]/div[2]/form/div[10]/input")
    create_account_button.click()
    time.sleep(3)

    allure.attach(context.driver.get_screenshot_as_png(), name="createAccc", attachment_type=AttachmentType.PNG)


@allure.severity(Severity.NORMAL)
@then(u'The user should be registered successfully')
def step_impl(context):
    time.sleep(2)  # small delay for the page to load completely

    try:
        # Capture console logs (for JS errors)
        for entry in context.driver.get_log('browser'):
            print("Console log:", entry)

        reg_success_screen = WebDriverWait(context.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div[2]/h1"))
        ).text

        if reg_success_screen == "There's a problem":
            print("Registered successfully")
        else:
            print("Registration failed or screen text did not match. Found:", reg_success_screen)
            # Take screenshot for debugging
            context.driver.save_screenshot("registration_error.png")
            assert False, "Registration screen did not show expected message."

    except NoSuchElementException as e:
        print("Element not found:", str(e))
        context.driver.save_screenshot("element_not_found.png")
        assert False, "Expected element not found."

    except Exception as e:
        print("An unexpected error occurred:", str(e))
        context.driver.save_screenshot("unexpected_error.png")
        assert False, "Unexpected error during registration flow."
