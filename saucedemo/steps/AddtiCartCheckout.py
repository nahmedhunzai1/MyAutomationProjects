
import time
from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException


chrome_options = Options()
chrome_options.add_argument("--incognito")
driver_path = "/Users/jerry/Desktop/QA-Automation/WHOZIN/driver/chrome-mac-arm64/chromedriver"


# @given(u'The user is on the signin page')
# def step_impl(context):
#
#     # Launch browser if not already done
#     if not hasattr(context, 'driver'):
#         context.driver = webdriver.Chrome()  # You can configure this as needed
#         context.driver.maximize_window()
#
#     context.driver.get("https://www.saucedemo.com/")  # Saucedemo login page



@allure.severity(allure.severity_level.CRITICAL)
@when(u'The user enters "standard_user" and "secret_sauce" -1')
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
    chrome_options.add_experimental_option("prefs", {
    "credentials_enable_service": False,
    "profile.password_manager_enabled": False})

@allure.severity(allure.severity_level.CRITICAL)
@when(u'The user should be signed in successfully')
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

@when(u'User must be able to search desired product')
def step_impl(context):
    add_to_cart_button = context.driver.find_element(By.XPATH,"//button[contains(@id, 'add-to-cart')]")
    add_to_cart_button.click()
    time.sleep(2)

    mini_cart_item = context.driver.find_element(By.XPATH,"//a[@data-test='shopping-cart-link']")
    mini_cart_item.click()
    time.sleep(2)

    allure.attach(context.driver.get_screenshot_as_png(), name="add_to_card",
                  attachment_type=allure.attachment_type.PNG)






@allure.severity(allure.severity_level.MINOR)
@when(u'User navigate to the product detail')
def step_impl(context):
    pass

@allure.severity(allure.severity_level.MINOR)
@when(u'User add product to cart')
def step_impl(context):
    pass

@allure.severity(allure.severity_level.TRIVIAL)
@then(u'User completes the checkout successfuly')
def step_impl(context):
    checkout_button = context.driver.find_element(By.XPATH,"//button[@id='checkout' or @name='checkout']")
    checkout_button.click()
    time.sleep(2)

    allure.attach(context.driver.get_screenshot_as_png(), name="form",
                  attachment_type=allure.attachment_type.PNG)

    first_name = context.driver.find_element(By.ID,ls
    "first-name")
    first_name.send_keys("Nadeem")
    time.sleep(1)

    last_name = context.driver.find_element(By.ID,"last-name")
    last_name.send_keys("Ahmed")
    time.sleep(1)

    postal_code = context.driver.find_element(By.ID,"postal-code")
    postal_code.send_keys("44220")
    time.sleep(1)

    continue_button = context.driver.find_element(By.XPATH,"/html/body/div/div/div/div[2]/div/form/div[2]/input")
    continue_button.click()
    time.sleep(1)

    finish_button = context.driver.find_element(By.XPATH,"/html/body/div/div/div/div[2]/div/div[2]/div[9]/button[2]")
    finish_button.click()

    time.sleep(1)

    allure.attach(context.driver.get_screenshot_as_png(), name="checkout_last_screen",
                  attachment_type=allure.attachment_type.PNG)

    back_to_home_button = context.driver.find_element(By.ID,"back-to-products")
    back_to_home_button.click()
    time.sleep(1)

    allure.attach(context.driver.get_screenshot_as_png(), name="back_to_home",
                  attachment_type=allure.attachment_type.PNG)







