import pickle

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
import random


chrome_options = Options()
chrome_options.add_argument("--incognito")
driver_path = "/Users/jerry/Desktop/QA-Automation/WHOZIN/driver/chrome-mac-arm64/chromedriver"


def generate_consultation():
    consultataion_title = [
        "Health Check-Up and Advice",
        "Legal Guidance Session",
        "Financial Planning Consultation",
        "Career Counseling",
        "Technology Troubleshooting",
        "Relationship Advice",
        "Fitness and Nutrition Planning",
        "Mental Wellness Check-In",
        "Business Strategy Discussion",
        "Parenting Support Session"
    ]

    consultation_description = [
        "A comprehensive session to address your health concerns and provide actionable advice.",
        "Get expert guidance on your legal matters to make informed decisions.",
        "Plan your finances effectively with tailored advice for your needs.",
        "Discuss your career goals and explore opportunities with a professional.",
        "Solve your tech issues and learn how to improve your digital experience.",
        "Receive personalized advice to navigate and strengthen your relationships.",
        "Achieve your fitness goals with a structured plan and nutritional guidance.",
        "Check in on your mental health and develop strategies for well-being.",
        "Explore innovative strategies to grow your business and increase efficiency.",
        "Discuss challenges and strategies for effective parenting."
    ]

    consultataion_title = random.choice(consultataion_title)
    consultation_description = random.choice(consultation_description)

    return consultataion_title, consultation_description


@allure.severity(allure.severity_level.CRITICAL)
@Given(u'User opens Konsuld URL-4')
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




@when(u'User click request konsuldation-4')
def step_impl(context):
    time.sleep(2)
    close_tutorial_button = context.driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div/div[1]/button")
    close_tutorial_button.click()
    time.sleep(2)

    request_consultation_button = context.driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/main/div/div[2]/div/div[2]/div/div[1]/div/div[1]/div/div/div/div[1]/div[1]/button")
    request_consultation_button.click()
    time.sleep(3)
    allure.attach(context.driver.get_screenshot_as_png(), name="testMessageInAccount",
                  attachment_type=AttachmentType.PNG)



@when(u'Enter the title and description-4')
def step_impl(context):
    title, description = generate_consultation()
    title_field = context.driver.find_element(By.XPATH,"/html/body/div[3]/div[3]/div/div[2]/form/div[1]/div[1]/div/div/input")
    title_field.send_keys(title)

    description_field = context.driver.find_element(By.XPATH,"/html/body/div[3]/div[3]/div/div[2]/form/div[1]/div[2]/div/div/textarea[1]")
    description_field.send_keys(description)

    time.sleep(2)

    allure.attach(context.driver.get_screenshot_as_png(), name="testMessageInAccount",
                  attachment_type=AttachmentType.PNG)



@when(u'Upload multiple videos-4')
def step_impl(context):
    # video_icon = context.driver.find_element(By.XPATH,"/html/body/div[3]/div[3]/div/div[2]/form/div[1]/div[3]/button[1]/span[1]/svg/path")
    # video_icon.click()
    # time.sleep(1)
    #
    # brows_file = context.driver.find_element(By.XPATH,"/html/body/div[3]/div[3]/div/div[2]/form/div[1]/div[3]/div[2]/div/div[1]/div/div/div/span/span")
    # brows_file.click()
    # time.sleep(2)

    pass




@when(u'Upload multiple images-4')
def step_impl(context):
    pass


@when(u'Add multiple URLs-4')
def step_impl(context):
    URL_option= context.driver.find_element(By.XPATH, "//button[@aria-label='Add URL']")
    URL_option.click()
    time.sleep(2)

    URL_Field = context.driver.find_element(By.XPATH,"/html/body/div[3]/div[3]/div/div[2]/form/div[1]/div[3]/div[2]/div/div[1]/div/div/div/input")
    URL_Field.send_keys("https://chatgpt.com/c/676aa60f-041c-800f-9cbc-c40d23f4f1ef")
    time.sleep(2)

    add_button = context.driver.find_element(By.XPATH,"/html/body/div[3]/div[3]/div/div[2]/form/div[1]/div[3]/div[2]/div/div[2]/button")
    add_button.click()
    time.sleep(1)

    allure.attach(context.driver.get_screenshot_as_png(), name="testMessageInAccount",
                  attachment_type=AttachmentType.PNG)


@when(u'Upload multiple documents-4')
def step_impl(context):
    pass


@when(u'Add multiple specialitites-4')
def step_impl(context):
    speciality_dropdown = context.driver.find_element(By.XPATH,"/html/body/div[3]/div[3]/div/div[2]/form/div[2]/div[2]/div/div/div/div/div[2]/button/span[1]")
    speciality_dropdown.click()
    time.sleep(2)

    speciality_one_checkbox = context.driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div/div[2]/form/div/div/div[2]/div/ul/li[1]/span/input")
    speciality_one_checkbox.click()


    speciality_two_checkbox = context.driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div/div[2]/form/div/div/div[2]/div/ul/li[2]/span/input")
    speciality_two_checkbox.click()
    time.sleep(1)
    allure.attach(context.driver.get_screenshot_as_png(), name="testMessageInAccount",
                  attachment_type=AttachmentType.PNG)

    done_button = context.driver.find_element(By.XPATH,"/html/body/div[3]/div[3]/div/div[3]/div/div[3]/button[2]")
    done_button.click()
    time.sleep(1)

    allure.attach(context.driver.get_screenshot_as_png(), name="testMessageInAccount",
                  attachment_type=AttachmentType.PNG)




@when(u'Add multiple focus Areas-4')
def step_impl(context):

    focus_area_scroll = context.driver.find_element(By.XPATH,"/html/body/div[3]/div[3]/div/div[2]/form/div[2]/div[3]/div/div/div/div/div[2]/button/span[1]")
    focus_area_scroll.click()
    time.sleep(1)

    focus_one_checkbox = context.driver.find_element(By.XPATH,"/html/body/div[3]/div[3]/div/div[2]/form/div/div/div[2]/div/ul/li[1]/ul/li[1]/span/input")
    focus_one_checkbox.click()

    focus_two_checkbox = context.driver.find_element(By.XPATH,"/html/body/div[3]/div[3]/div/div[2]/form/div/div/div[2]/div/ul/li[1]/ul/li[2]/span/input")
    focus_two_checkbox.click()
    time.sleep(1)

    done_button = context.driver.find_element(By.XPATH,"/html/body/div[3]/div[3]/div/div[3]/div/div[3]/button[2]")
    done_button.click()
    time.sleep(1)

    allure.attach(context.driver.get_screenshot_as_png(), name="testMessageInAccount",
                  attachment_type=AttachmentType.PNG)


@when(u'Click Request Konsuldation button and verify the success message-4')
def step_impl(context):
    create_consultation_button = context.driver.find_element(By.XPATH,"/html/body/div[3]/div[3]/div/div[3]/div/button/span[1]")
    create_consultation_button.click()
    time.sleep(3)

    allure.attach(context.driver.get_screenshot_as_png(), name="testMessageInAccount",
                  attachment_type=AttachmentType.PNG)



@then(u'The Konsuldation is created and it appears on home page-4')
def step_impl(context):
    pass
