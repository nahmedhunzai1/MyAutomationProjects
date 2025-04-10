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
@Given(u'User opens Konsuld URL-5')
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

@when(u'click Log In button-5')
def step_impl(context):
    login_button = context.driver.find_element(By.XPATH, "/html/body/div/div[1]/main/div/div/div/div/div/div/button[1]")
    login_button.click()
    time.sleep(2)
    allure.attach(context.driver.get_screenshot_as_png(), name="testMessageInAccount",
                  attachment_type=AttachmentType.PNG)

@when(u'enter email and password-5')
def step_impl(context):
    email_field = context.driver.find_element(By.ID, 'email')
    email_field.send_keys('sand-aid@hbiujzoo.mailosaur.net')
    password_field = context.driver.find_element(By.ID, "password")
    password_field.send_keys('Admin@123')
    allure.attach(context.driver.get_screenshot_as_png(), name="testMessageInAccount",
                  attachment_type=AttachmentType.PNG)

@when(u'click Sign In button-5')
def step_impl(context):
    sign_in_button = context.driver.find_element(By.XPATH,
                                                 '//*[@id="root"]/div[1]/main/div/div[2]/div[1]/form/div/div/button')
    sign_in_button.click()
    allure.attach(context.driver.get_screenshot_as_png(), name="testMessageInAccount",
                  attachment_type=AttachmentType.PNG)
    time.sleep(8)


@when(u'Get the verfication code from mailosaurs inbox-5')
def step_impl(context):
    api_key = "JaT3k75qDJr7Uv41R1zIj5qiyz129vrn"
    server_id = "hbiujzoo"
    server_domain = "hbiujzoo.mailosaur.net"

    mailosaur = MailosaurClient(api_key)
    criteria = SearchCriteria()
    criteria.sent_to = "sand-aid@" + server_domain

    # Get the email
    email = mailosaur.messages.get(server_id, criteria)
    print("Subject: " + email.subject)
    message = mailosaur.messages.get(server_id, criteria)

    # Get the first verification code
    first_code = message.html.codes[0]
    print(first_code.value)  # Prints the verification code, e.g., "456812"

    # Store the verification code in context for use in other steps
    context.verification_code = first_code.value


@when(u'enter it in the verification code section-5')
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




@when(u'click confirm-5')
def step_impl(context):
    confirm_button = context.driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/main/div/div[2]/div/div/div/form/div/button")
    confirm_button.click()

    time.sleep(5)
    allure.attach(context.driver.get_screenshot_as_png(), name="testMessageInAccount",
                  attachment_type=AttachmentType.PNG)




@When(u'user must login the app-5')
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
        allure.attach(context.driver.get_screenshot_as_png(), name="testMessageInAccount",
                      attachment_type=AttachmentType.PNG)


        time.sleep(3)




@When(u'User is present on the home page-5')
def step_impl(context):
    pass


@when(u'User searches the other user #Oliver George#-5')
def step_impl(context):
    time.sleep(2)
    close_tutorial_button = context.driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div/div[1]/button")
    close_tutorial_button.click()
    time.sleep(2)

    search_filter = context.driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/main/div/div[1]/header/div/div/div[1]/div/div/div/div/div/input")
    search_filter.click()

    search_filter.send_keys("Oliver George")
    time.sleep(1)

    allure.attach(context.driver.get_screenshot_as_png(), name="testMessageInAccount",
                  attachment_type=AttachmentType.PNG)




@when(u'Selects posts option from dropdown-5')
def step_impl(context):
    post_option = context.driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/main/div/div[1]/header/div/div/div[1]/div/div/div[2]/div/ul/li/ul/li[3]/div[2]/div[1]/span")
    post_option.click()
    time.sleep(3)
    allure.attach(context.driver.get_screenshot_as_png(), name="testMessageInAccount",
                  attachment_type=AttachmentType.PNG)





@when(u'Click through the first post appearing and navigate to post detail-5')
def step_impl(context):
    first_post = context.driver.find_element(By.XPATH,
                                             "/html/body/div[1]/div[1]/main/div/div[2]/div/div[2]/div/div[2]/div/div/div/div/div/div/div/div[2]/div/a[1]/span")
    first_post.click()
    time.sleep(3)

    allure.attach(context.driver.get_screenshot_as_png(), name="testMessageInAccount",
                  attachment_type=AttachmentType.PNG)


@when(u'User Likes and Comments on the post-5')
def step_impl(context):
    like_post = context.driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/main/div/div[2]/div/div[2]/div/div[1]/div/div[2]/div/div[2]/div/div/button[1]")
    like_post.click()
    time.sleep(3)

    comment_section = context.driver.find_element(By.XPATH,"//button[@aria-label='Comment Button']")
    comment_section.click()
    time.sleep(2)

    comment_field = context.driver.find_element(By.XPATH,"//button[@aria-label='Comment Button']/following::textarea[1]")
    comment_field.send_keys("Cool post , it does have alot information ")
    time.sleep(2)

    allure.attach(context.driver.get_screenshot_as_png(), name="testMessageInAccount",
                  attachment_type=AttachmentType.PNG)

    post_button = context.driver.find_element(By.XPATH,"//button[.//span[text()='POST']]")
    post_button.click()
    time.sleep(5)

    allure.attach(context.driver.get_screenshot_as_png(), name="testMessageInAccount",
                  attachment_type=AttachmentType.PNG)


