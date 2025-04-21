import time

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
from selenium.webdriver.chrome.options import Options


chrome_options = Options()
chrome_options.add_argument("--incognito")
driver_path = "/Users/jerry/Desktop/QA-Automation/WHOZIN/driver/chrome-mac-arm64/chromedriver"


@given(u'The user is on the signin page')
def step_impl(context):

    # Launch browser if not already done
    if not hasattr(context, 'driver'):
        context.driver = webdriver.Chrome()  # You can configure this as needed
        context.driver.maximize_window()

    context.driver.get("https://www.saucedemo.com/")  # Saucedemo login page




@when(u'The user enters "{username}" and "secret_sauce"')
def step_impl(context, username):
    wait = WebDriverWait(context.driver, 10)
    username_input = wait.until(EC.presence_of_element_located((By.ID, "user-name")))
    password_input = context.driver.find_element(By.ID, "password")
    login_button = context.driver.find_element(By.ID, "login-button")

    # username_input.clear()
    # password_input.clear()
    username_input.send_keys(username)
    time.sleep(1)
    password_input.send_keys("secret_sauce")
    time.sleep(1)
    login_button.click()
    time.sleep(3)


@then(u'The user should be signed in successfully')
def step_impl(context):
    try:
        # Wait for the presence of the inventory container
        WebDriverWait(context.driver, 5).until(
            EC.presence_of_element_located((By.ID, "inventory_container"))
        )
        assert "inventory.html" in context.driver.current_url
        print("✅ Login successful")
    except Exception as e:
        # Attach screenshot if login fails
        allure.attach(context.driver.get_screenshot_as_png(), name="login_failure",
                      attachment_type=allure.attachment_type.PNG)
        print("❌ Login failed")
        raise e
