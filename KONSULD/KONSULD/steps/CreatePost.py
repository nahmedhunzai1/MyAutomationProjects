from selenium.webdriver.support import expected_conditions as EC
from mailosaur import MailosaurClient
from mailosaur.models import SearchCriteria
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
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
         "Stress Management and Relaxation Techniques",
        "Personalized Study Plan Session",
        "Home Renovation Planning",
        "Social Media Growth Strategy",
        "Dietary Allergy Consultation",
        "Small Business Financial Coaching",
        "Pet Care and Training Tips",
        "Travel Planning Assistance",
        "Event Coordination Consultation",
        "Language Learning Guidance"
    ]

    consultation_description = [
        "Learn effective methods to manage stress and find inner calm with expert advice.",
        "Create a customized study plan to maximize productivity and achieve your learning goals.",
        "Plan your dream home renovation with detailed guidance on design and budget.",
        "Boost your online presence with proven strategies for social media growth.",
        "Discuss your dietary needs and manage allergies with a specialized nutritionist.",
        "Gain insights into managing your small business finances and increasing profitability.",
        "Get expert tips on training and caring for your beloved pets.",
        "Plan your next adventure with personalized travel itineraries and tips.",
        "Organize memorable events with step-by-step guidance on planning and coordination.",
        "Learn effective techniques to master a new language with the help of a tutor."
    ]

    consultataion_title = random.choice(consultataion_title)
    consultation_description = random.choice(consultation_description)

    return consultataion_title, consultation_description




@allure.severity(allure.severity_level.CRITICAL)
@Given(u'User opens Konsuld URL-3')
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

@when(u'click Log In button-3')
def step_impl(context):
    login_button = context.driver.find_element(By.XPATH, "/html/body/div/div[1]/main/div/div/div/div/div/div/button[1]")
    login_button.click()
    time.sleep(2)
    allure.attach(context.driver.get_screenshot_as_png(), name="testMessageInAccount",
                  attachment_type=AttachmentType.PNG)

@when(u'enter email and password-3')
def step_impl(context):
    email_field = context.driver.find_element(By.ID, 'email')
    email_field.send_keys('nahmed@ohkfhtut.mailosaur.net')
    password_field = context.driver.find_element(By.ID, "password")
    password_field.send_keys('Admin@123')
    allure.attach(context.driver.get_screenshot_as_png(), name="testMessageInAccount",
                  attachment_type=AttachmentType.PNG)

@when(u'click Sign In button-3')
def step_impl(context):
    sign_in_button = context.driver.find_element(By.XPATH,
                                                 '//*[@id="root"]/div[1]/main/div/div[2]/div[1]/form/div/div/button')
    sign_in_button.click()
    allure.attach(context.driver.get_screenshot_as_png(), name="testMessageInAccount",
                  attachment_type=AttachmentType.PNG)
    time.sleep(8)


@when(u'Get the verfication code from mailosaurs inbox-3')
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


@when(u'enter it in the verification code section-3')
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




@when(u'click confirm-3')
def step_impl(context):
    confirm_button = context.driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/main/div/div[2]/div/div/div/form/div/button")
    confirm_button.click()

    time.sleep(5)
    allure.attach(context.driver.get_screenshot_as_png(), name="testMessageInAccount",
                  attachment_type=AttachmentType.PNG)

    time.sleep(2)
    close_tutorial_button = context.driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div/div[1]/button")
    close_tutorial_button.click()
    time.sleep(2)


@Then(u'user must login the app-3')
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




@Then(u'User is present on the home page-3')
def step_impl(context):
    pass


@when(u'User click Create Post button-3')
def step_impl(context):
    create_post_button = context.driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/main/div/div[2]/div/div[2]/div/div[1]/div/div[1]/div/div/div/div[1]/div[2]/button")
    create_post_button.click()
    time.sleep(2)
    allure.attach(context.driver.get_screenshot_as_png(), name="testMessageInAccount",
                  attachment_type=AttachmentType.PNG)


@when(u'Enter the title and description-3')
def step_impl(context):
    title, description = generate_consultation()


    title_field = context.driver.find_element(By.XPATH,"/html/body/div[3]/div[3]/div/div[2]/form/div/div[1]/div/div/input")
    title_field.send_keys(title)
    time.sleep(1)

    description_field = context.driver.find_element(By.XPATH,"/html/body/div[3]/div[3]/div/div[2]/form/div/div[2]/div/div/textarea[1]")
    description_field.send_keys(description)

    allure.attach(context.driver.get_screenshot_as_png(), name="testMessageInAccount",
                  attachment_type=AttachmentType.PNG)




@when(u'Upload multiple videos-3')
def step_impl(context):
    pass


@when(u'Upload multiple images-3')
def step_impl(context):
    pass


@when(u'Add multiple URLs-3')
def step_impl(context):
    URL_button = context.driver.find_element(By.XPATH,"/html/body/div[3]/div[3]/div/div[2]/form/div/div[3]/button[2]")
    URL_button.click()
    time.sleep(1)

    url_field = context.driver.find_element(By.XPATH,"/html/body/div[3]/div[3]/div/div[2]/form/div/div[3]/div[2]/div/div[1]/div/div/div/input")
    url_field.send_keys("https://dev.konsuld.app/home")

    add_button = context.driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div/div[2]/form/div/div[3]/div[2]/div/div[2]/button")
    add_button.click()
    time.sleep(2)
    allure.attach(context.driver.get_screenshot_as_png(), name="testMessageInAccount",
                  attachment_type=AttachmentType.PNG)

    URL_button = context.driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div/div[2]/form/div/div[4]/button[2]")
    URL_button.click()
    time.sleep(1)

    url_field = context.driver.find_element(By.XPATH,
                                            "//html/body/div[3]/div[3]/div/div[2]/form/div/div[4]/div[2]/div/div[1]/div/div/div/input")
    url_field.send_keys("https://dev.konsuld.app/home")

    add_button = context.driver.find_element(By.XPATH,
                                             "/html/body/div[3]/div[3]/div/div[2]/form/div/div[4]/div[2]/div/div[2]/button")
    add_button.click()
    time.sleep(1)

    allure.attach(context.driver.get_screenshot_as_png(), name="testMessageInAccount",
                  attachment_type=AttachmentType.PNG)



@when(u'Upload multiple documents-3')
def step_impl(context):
    pass


@when(u'Click Create Post button and verify the success message-3')
def step_impl(context):
    create_post_button = context.driver.find_element(By.XPATH,"/html/body/div[3]/div[3]/div/div[3]/button")
    create_post_button.click()
    time.sleep(2)

    allure.attach(context.driver.get_screenshot_as_png(), name="testMessageInAccount",
                  attachment_type=AttachmentType.PNG)


@then(u'The Post is created and it appears on home page-3')
def step_impl(context):
    pass





@When(u'user must login the app-3')
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




@When(u'User is present on the home page-3')
def step_impl(context):
    pass