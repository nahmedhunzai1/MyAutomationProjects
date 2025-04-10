import pickle
from sys import exception

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
@given(u'User opens Konsuld URL-6')
def step_impl(context):
    try:
        auth_token = pickle.load(open("../test-cases/chndler.pkl", "rb"))
        if auth_token:
            print(f"Auth Token Loaded: {auth_token}")
        else:
            print("Auth token not found in pickle.")
            auth_token = None
    except Exception as e:
        print(f"Error loading auth token: {e}")
        auth_token = None

    # Initialize the browser
    context.driver = webdriver.Chrome(options=chrome_options)
    context.driver.maximize_window()

    # Open the website
    context.driver.get("https://dev.konsuld.app/")

    # Wait for the page to load before setting localStorage
    time.sleep(2)

    # Set the auth token to localStorage if it exists
    if auth_token:
        context.driver.execute_script(f"""
            window.localStorage.setItem('access_token', '{auth_token}');
            window.localStorage.setItem('refresh_token', '{auth_token}');
        """)

    # Refresh the page to ensure the localStorage is properly set
    context.driver.refresh()

    time.sleep(4)






@When(u'user must login the app-6')
def step_impl(context):
    pass


@When(u'User is present on the home page-6')
def step_impl(context):
    pass


@when(u'User searches the other user #Oliver George#-6')
def step_impl(context):
    time.sleep(2)
    close_tutorial_button = context.driver.find_element(By.XPATH, "//button[contains(@aria-label, 'close')]")
    close_tutorial_button.click()
    time.sleep(2)

    search_filter = context.driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/main/div/div[1]/header/div/div/div[1]/div/div/div/div/div/input")
    search_filter.click()

    search_filter.send_keys("oliver new")
    time.sleep(1)

    allure.attach(context.driver.get_screenshot_as_png(), name="testMessageInAccount",
                  attachment_type=AttachmentType.PNG)




@when(u'Selects posts option from dropdown-6')
def step_impl(context):
    try:
        post_option = context.driver.find_element(By.XPATH,
                                              '//div[contains(@class, "MuiListItemText-root")]//span[contains(@class, "MuiTypography-root")]')
        time.sleep(2)

        print("hi im here ")

        post_option.click()
        time.sleep(4)
        allure.attach(context.driver.get_screenshot_as_png(), name="testMessageInAccount",
                    attachment_type=AttachmentType.PNG)
    except Exception as e:
        print(f"An error occurred: {e}")



@when(u'Click other users profile-6')
def step_impl(context):
    user_profile = context.driver.find_element(By.XPATH,"//div[contains(@class, 'MuiBox-root')]//span[contains(@class, 'MuiTypography-root')]//span[normalize-space()]")
    user_profile.click()
    time.sleep(3)
    allure.attach(context.driver.get_screenshot_as_png(), name="testMessageInAccount",
                  attachment_type=AttachmentType.PNG)


@when(u'Click connect button-6')
def step_impl(context):
    # connect_button = context.driver.find_element(By.XPATH,"//*[@id='root']/div[1]/main/div/div[2]/div/div[2]/div/div[1]/div[2]/div/div[2]/div[2]/div/button[1]/span[2]")
    # connect_button.click()
    # context.driver.implicitly_wait(10)

    connect_button = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH,
                                    "//*[@id='root']/div[1]/main/div/div[2]/div/div[2]/div/div[1]/div[2]/div/div[2]/div[2]/div/button[1]/span[2]"))
    )
    connect_button.click()

    time.sleep(3)

    button_text = context.driver.find_element(By.XPATH,"//*[@id='root']/div[1]/main/div/div[2]/div/div[2]/div/div[1]/div[2]/div/div[2]/div[2]/div/div/span").text
    print("The button text is",button_text)
    if button_text == 'Pending':
        print('successfully request sent')
    else:
        raise Exception("Request not sent")
    allure.attach(context.driver.get_screenshot_as_png(), name="testMessageInAccount",
                  attachment_type=AttachmentType.PNG)


@when(u'User opens Konsuld URL-7')
def step_impl(context):
    try:
        auth_token = pickle.load(open("../test-cases/oliver.pkl", "rb"))
        if auth_token:
            print(f"Auth Token Loaded: {auth_token}")
        else:
            print("Auth token not found in pickle.")
            auth_token = None
    except Exception as e:
        print(f"Error loading auth token: {e}")
        auth_token = None

    # Initialize the browser
    context.driver = webdriver.Chrome(options=chrome_options)
    context.driver.maximize_window()

    # Open the website
    context.driver.get("https://dev.konsuld.app/")

    # Wait for the page to load before setting localStorage
    time.sleep(2)

    # Set the auth token to localStorage if it exists
    if auth_token:
        context.driver.execute_script(f"""
            window.localStorage.setItem('access_token', '{auth_token}');
            window.localStorage.setItem('refresh_token', '{auth_token}');
        """)

    # Refresh the page to ensure the localStorage is properly set
    context.driver.refresh()
    time.sleep(1)
    context.driver.refresh()

    time.sleep(10)





@when(u'user must login the app-7')
def step_impl(context):
    close_tutorial_button = context.driver.find_element(By.XPATH, "//button[contains(@aria-label, 'close')]")
    close_tutorial_button.click()
    time.sleep(1)
    allure.attach(context.driver.get_screenshot_as_png(), name="testMessageInAccount",
                  attachment_type=AttachmentType.PNG)


@when(u'User is present on the home page-7')
def step_impl(context):
    pass


@when(u'User opens notification-7')
def step_impl(context):
    notification_button = context.driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/main/div/div[1]/header/div/div/div[2]/div[1]/div[3]/div/div")
    notification_button.click()
    time.sleep(3)

    user_profile_button = context.driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/main/div/div[2]/div/div[2]/div/div[1]/div/div[2]/div/div/div/div[1]/div/div/div/div[1]/div/div[2]/span/span/span")
    user_profile_button.click()
    time.sleep(4)

    allure.attach(context.driver.get_screenshot_as_png(), name="testMessageInAccount",
                  attachment_type=AttachmentType.PNG)


@when(u'Accepts connect requesst-7')
def step_impl(context):
    accept_request_button = context.driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/main/div/div[2]/div/div[2]/div/div[1]/div[2]/div/div[2]/div[2]/div/div/button[2]/span[1]")
    accept_request_button.click()
    time.sleep(5)

    message_button_text = context.driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/main/div/div[2]/div/div[2]/div/div[1]/div[2]/div/div[2]/div[2]/div/button[1]/span[1]").text

    if message_button_text == "Message":
        print("Connect Request is successfully accepted")
    else:
        raise Exception("Connect Request failed to accpet")

    allure.attach(context.driver.get_screenshot_as_png(), name="testMessageInAccount",
                  attachment_type=AttachmentType.PNG)


@then(u'Disconnects  Request-7')
def step_impl(context):
    menu_dropdown = context.driver.find_element(By.XPATH,"//button[@class='MuiButtonBase-root MuiIconButton-root MuiIconButton-sizeMedium css-4mtax3']")
    menu_dropdown.click()
    time.sleep(1)

    allure.attach(context.driver.get_screenshot_as_png(), name="testMessageInAccount",
                  attachment_type=AttachmentType.PNG)

    disconnect_button = context.driver.find_element(By.XPATH,"/html/body/div[3]/div[3]/ul/li[1]/span[1]")
    disconnect_button.click()
    time.sleep(2)

    allure.attach(context.driver.get_screenshot_as_png(), name="testMessageInAccount",
                  attachment_type=AttachmentType.PNG)

    popup_disconnect_button = context.driver.find_element(By.XPATH,"/html/body/div[3]/div[3]/div/div[2]/button[2]/span[1]")
    popup_disconnect_button.click()
    time.sleep(3)

    allure.attach(context.driver.get_screenshot_as_png(), name="testMessageInAccount",
                  attachment_type=AttachmentType.PNG)









