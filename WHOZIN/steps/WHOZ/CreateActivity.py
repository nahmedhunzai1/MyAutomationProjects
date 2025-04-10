from lib2to3.fixes.fix_input import context
from lib2to3.pgen2 import driver
from selenium import webdriver
from behave import *
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


@when(u'Verify Create Activity happy flow is working fine')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get("https://uat.app.whoz.co")
    time.sleep(6)
    login_with_google = context.driver.find_element(By.XPATH,'//*[@id="root"]/div[2]/div/main/div[2]/div/div/div/div/div[1]/form/div[2]/button/p')
    login_with_google.click()
    time.sleep(4)

    google_email = context.driver.find_element(By.XPATH, '//*[@id="identifierId"]')
    google_email.send_keys("nahmed@technologyrivers.com")
    time.sleep(2)

    click_next_button = context.driver.find_element(By.XPATH, '//*[@id="identifierNext"]/div/button/span')
    click_next_button.click()
    time.sleep(3)

    email_password = context.driver.find_element(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input')
    email_password.send_keys('Technologyrivers@123')
    time.sleep(2)

    context.driver.find_element(By.XPATH, '//*[@id="passwordNext"]/div/button/span').click()
    time.sleep(5)

    click_continue_button = context.driver.find_element(By.XPATH,
                                                        '/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[3]/div/div/div[2]/div/div/button/span')
    click_continue_button.click()
    time.sleep(10)

    create_activity_button = context.driver.find_element(By.XPATH,
                                                         '/html/body/div[1]/div[2]/header/div/div/div[2]/button[1]')
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

    activity_description = context.driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/div/div[2]/div/div[2]/div/div/div[3]/div/div[3]/div/div/textarea[1]')
    activity_description.send_keys(random_activity_name)

    time.sleep(2)

    max_guet = context.driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/div/div[2]/div/div[2]/div/div/div[3]/div/div[4]/div/input')
    max_guet.send_keys('5')
    time.sleep(3)

    click_next_button = context.driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/div/div[2]/div/div[2]/div/div/div[3]/div/div[6]/button[2]')
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

    start_date_menu = context.driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/div/div[2]/div/div[2]/div/div/div[3]/div/div[1]/div[2]/div/div/div[2]/div/div/div/button')
    start_date_menu.click()
    time.sleep(2)

    select_start_date = context.driver.find_element(By.XPATH,'/html/body/div[3]/div[2]/div/div[1]/div/ul[1]/li[2]')
    select_start_date.click()
    time.sleep(3)

    end_date_menu = context.driver.find_element (By.XPATH,'//*[@id="root"]/div[2]/div/div/div[2]/div/div[2]/div/div/div[3]/div/div[1]/div[2]/div/div/div[3]/div/div/div/button')
    end_date_menu.click()
    time.sleep(3)

    select_end_time = context.driver.find_element (By.XPATH,'/html/body/div[3]/div[2]/div/div[1]/div/ul[1]/li[3]')
    select_end_time.click()
    time.sleep(1)

    ok_button = context.driver.find_element(By.XPATH,'/html/body/div[3]/div[2]/div/div[2]/button[2]')
    ok_button.click()
    time.sleep(2)

    context.driver.execute_script("window.scrollTo(0, 500);")
    time.sleep(2)

    location_field = context.driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/div/div[2]/div/div[2]/div/div/div[3]/div/div[3]/div[2]/div[2]/div/div/div/input')
    location_field.send_keys('office')
    time.sleep(5)

    google_fetched_location = context.driver.find_element(By.XPATH,'//*[@id="google-map-demo-option-0"]')
    google_fetched_location.click()
    time.sleep(5)

    next_button_second_screen = context.driver.find_element(By.XPATH,'//*[@id="root"]/div[2]/div/div/div[2]/div/div[2]/div/div/div[3]/div/div[5]/button[2]')
    next_button_second_screen.click()
    time.sleep(2)

    context.driver.execute_script("window.scrollTo(0, 0);")
    time.sleep(2)

    brows_contact_button = context.driver.find_element(By.XPATH,'//*[@id="root"]/div[2]/div/div/div[2]/div/div[2]/div/div/div[3]/div/div[2]/button')
    brows_contact_button.click()
    time.sleep(2)

    expand_all_contacts = context.driver.find_element(By.XPATH,'//*[@id="panel1a-header"]/div[2]')
    expand_all_contacts.click()
    time.sleep(6)

    contacts_checkbox = context.driver.find_element(By.XPATH,'//*[@id="panel1a-content"]/div/div/div[1]/div/div[2]/div[1]/div/div/div[1]/div[1]/div/div/span/input')
    contacts_checkbox.click()
    time.sleep(2)

    done_button_contacts = context.driver.find_element(By.XPATH,'//*[@id="root"]/div[2]/div/div/div[2]/div/div[1]/div[2]/button')
    done_button_contacts.click()
    time.sleep(2)

    context.driver.execute_script("window.scrollTo(0, 500);")
    time.sleep(2)

    next_button_third_screen = context.driver.find_element(By.XPATH,'//*[@id="root"]/div[2]/div/div/div[2]/div/div[2]/div/div/div[3]/div/div[6]/button[2]')
    next_button_third_screen.click()
    time.sleep(2)

    send_invites_button = context.driver.find_element(By.XPATH,'//*[@id="root"]/div[2]/div/div/div[2]/div/div[2]/div/div/div[3]/div/div[3]/button[2]')
    send_invites_button.click()
    time.sleep(2)

    context.driver.execute_script("window.scrollTo(0, 500);")
    time.sleep(2)

    view_activity_button = context.driver.find_element(By.XPATH,'/html/body/div[3]/div[3]/div/div/div[3]/button')
    view_activity_button.click()
    time.sleep(2)








