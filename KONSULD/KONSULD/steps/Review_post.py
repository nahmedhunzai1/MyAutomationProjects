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
        "Health Check-Up and Advice Konsuldation",
        "Legal Guidance Session Konsuldation",
        "Financial Planning Consultation Konsuldation",
        "Career Counseling Konsuldation",
        "Technology Troubleshooting Konsuldation",
        "Relationship Advice Konsuldation",
        "Fitness and Nutrition Planning Konsuldation",
        "Mental Wellness Check-In Konsuldation",
        "Business Strategy Discussion Konsuldation",
        "Parenting Support Session Konsuldation"
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
@given(u'Given User opens Konsuld URL-RP')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get("https://dev.konsuld.app/")
    time.sleep(3)
    allure.attach(context.driver.get_screenshot_as_png(), name="login",
                  attachment_type=AttachmentType.PNG)


@allure.severity(allure.severity_level.CRITICAL)
@when(u'click Log In button-RP')
def step_impl(context):
    login_button = context.driver.find_element(By.XPATH, "/html/body/div/div[1]/main/div/div/div/div/div/div/button[1]")
    login_button.click()
    time.sleep(2)
    allure.attach(context.driver.get_screenshot_as_png(), name="login",
                  attachment_type=AttachmentType.PNG)

@allure.severity(allure.severity_level.CRITICAL)
@when(u'enter email and password-RP')
def step_impl(context):
    email_field = context.driver.find_element(By.ID, 'email')
    email_field.send_keys('sand-aid@hbiujzoo.mailosaur.net')
    password_field = context.driver.find_element(By.ID, "password")
    password_field.send_keys('Admin@123')
    allure.attach(context.driver.get_screenshot_as_png(), name="login",
                  attachment_type=AttachmentType.PNG)

@allure.severity(allure.severity_level.CRITICAL)
@when(u'click Sign In button-RP')
def step_impl(context):
    sign_in_button = context.driver.find_element(By.XPATH,
                                                 '//*[@id="root"]/div[1]/main/div/div[2]/div[1]/form/div/div/button')
    sign_in_button.click()
    allure.attach(context.driver.get_screenshot_as_png(), name="login",
                  attachment_type=AttachmentType.PNG)
    time.sleep(8)

@allure.severity(allure.severity_level.CRITICAL)
@when(u'Get the verfication code from mailosaurs inbox-RP')
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

@allure.severity(allure.severity_level.CRITICAL)
@when(u'enter it in the verification code section-RP')
def step_impl(context):
    # Retrieve the verification code from context
    verification_code = context.verification_code

    # Find the verification code input field and enter the code
    verification_code_field = context.driver.find_element(By.XPATH,
                                                          "//input[starts-with(@id, 'verification_code')]")
    verification_code_field.send_keys(verification_code)
    time.sleep(2)
    allure.attach(context.driver.get_screenshot_as_png(), name="login",
                  attachment_type=AttachmentType.PNG)

@allure.severity(allure.severity_level.CRITICAL)
@when(u'click confirm-RP')
def step_impl(context):
    confirm_button = context.driver.find_element(By.XPATH,
                                                 "/html/body/div[1]/div[1]/main/div/div[2]/div/div/div/form/div/button")
    confirm_button.click()

    time.sleep(5)
    allure.attach(context.driver.get_screenshot_as_png(), name="login",
                  attachment_type=AttachmentType.PNG)

@allure.severity(allure.severity_level.CRITICAL)
@when(u'user must login the app-RP')
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
        allure.attach(context.driver.get_screenshot_as_png(), name="login",
                      attachment_type=AttachmentType.PNG)

        time.sleep(3)

@allure.severity(allure.severity_level.NORMAL)
@when(u'User is present on the home page-RP')
def step_impl(context):
    time.sleep(2)
    close_tutorial_button = context.driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div/div[1]/button")
    close_tutorial_button.click()
    time.sleep(2)

@allure.severity(allure.severity_level.CRITICAL)
@when(u'User click request konsuldation-RP')
def step_impl(context):
    request_consultation_button = context.driver.find_element(By.XPATH,
                                                              "/html/body/div[1]/div[1]/main/div/div[2]/div/div[2]/div/div[1]/div/div[1]/div/div/div/div[1]/div[1]/button")
    request_consultation_button.click()
    time.sleep(3)
    allure.attach(context.driver.get_screenshot_as_png(), name="CreateKonsuldation",
                  attachment_type=AttachmentType.PNG)

@allure.severity(allure.severity_level.CRITICAL)
@when(u'Enter the title and description-RP')
def step_impl(context):
    title, description = generate_consultation()
    title_field = context.driver.find_element(By.XPATH,
                                              "/html/body/div[3]/div[3]/div/div[2]/form/div[1]/div[1]/div/div/input")
    title_field.send_keys(title)

    description_field = context.driver.find_element(By.XPATH,
                                                    "/html/body/div[3]/div[3]/div/div[2]/form/div[1]/div[2]/div/div/textarea[1]")
    description_field.send_keys(description)

    time.sleep(2)

    allure.attach(context.driver.get_screenshot_as_png(), name="CreateKonsuldation",
                  attachment_type=AttachmentType.PNG)

@allure.severity(allure.severity_level.NORMAL)
@when(u'Upload multiple videos-RP')
def step_impl(context):
    pass

@allure.severity(allure.severity_level.NORMAL)
@when(u'Upload multiple images-RP')
def step_impl(context):
    pass

@allure.severity(allure.severity_level.NORMAL)
@when(u'Add multiple URLs-RP')
def step_impl(context):
    URL_option = context.driver.find_element(By.XPATH, "//button[@aria-label='Add URL']")
    URL_option.click()
    time.sleep(2)

    URL_Field = context.driver.find_element(By.XPATH,
                                            "/html/body/div[3]/div[3]/div/div[2]/form/div[1]/div[3]/div[2]/div/div[1]/div/div/div/input")
    URL_Field.send_keys("https://chatgpt.com/c/676aa60f-041c-800f-9cbc-c40d23f4f1ef")
    time.sleep(2)

    add_button = context.driver.find_element(By.XPATH,
                                             "/html/body/div[3]/div[3]/div/div[2]/form/div[1]/div[3]/div[2]/div/div[2]/button")
    add_button.click()
    time.sleep(1)

    allure.attach(context.driver.get_screenshot_as_png(), name="CreateKonsuldation",
                  attachment_type=AttachmentType.PNG)

@allure.severity(allure.severity_level.MINOR)
@when(u'Upload multiple documents-RP')
def step_impl(context):
    pass

@allure.severity(allure.severity_level.CRITICAL)
@when(u'Add multiple specialitites-RP')
def step_impl(context):
    speciality_dropdown = context.driver.find_element(By.XPATH,
                                                      "/html/body/div[3]/div[3]/div/div[2]/form/div[2]/div[2]/div/div/div/div/div[2]/button/span[1]")
    speciality_dropdown.click()
    time.sleep(2)

    speciality_one_checkbox = context.driver.find_element(By.XPATH,
                                                          "/html/body/div[3]/div[3]/div/div[2]/form/div/div/div[2]/div/ul/li[1]/span/input")
    speciality_one_checkbox.click()

    speciality_two_checkbox = context.driver.find_element(By.XPATH,
                                                          "/html/body/div[3]/div[3]/div/div[2]/form/div/div/div[2]/div/ul/li[2]/span/input")
    speciality_two_checkbox.click()
    time.sleep(1)

    done_button = context.driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div/div[3]/div/div[3]/button[2]")
    done_button.click()
    time.sleep(2)

    allure.attach(context.driver.get_screenshot_as_png(), name="CreateKonsuldation",
                  attachment_type=AttachmentType.PNG)

@allure.severity(allure.severity_level.CRITICAL)
@when(u'Add multiple focus Areas-RP')
def step_impl(context):
    focus_area_scroll = context.driver.find_element(By.XPATH,
                                                    "/html/body/div[3]/div[3]/div/div[2]/form/div[2]/div[3]/div/div/div/div/div[2]/button/span[1]")
    focus_area_scroll.click()
    time.sleep(1)

    focus_one_checkbox = context.driver.find_element(By.XPATH,
                                                     "/html/body/div[3]/div[3]/div/div[2]/form/div/div/div[2]/div/ul/li[1]/ul/li[1]/span/input")
    focus_one_checkbox.click()

    focus_two_checkbox = context.driver.find_element(By.XPATH,
                                                     "/html/body/div[3]/div[3]/div/div[2]/form/div/div/div[2]/div/ul/li[1]/ul/li[2]/span/input")
    focus_two_checkbox.click()
    time.sleep(1)

    done_button = context.driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div/div[3]/div/div[3]/button[2]")
    done_button.click()
    time.sleep(2)

    allure.attach(context.driver.get_screenshot_as_png(), name="CreateKonsuldation",
                  attachment_type=AttachmentType.PNG)

@allure.severity(allure.severity_level.CRITICAL)
@when(u'Click Request Konsuldation button and verify the success message-RP')
def step_impl(context):
    create_consultation_button = context.driver.find_element(By.XPATH,
                                                             "/html/body/div[3]/div[3]/div/div[3]/div/button/span[1]")
    create_consultation_button.click()
    time.sleep(3)



@allure.severity(allure.severity_level.MINOR)
@then(u'The Konsuldation is created and it appears on home page-RP')
def step_impl(context):
    pass

# -----------------------------------------------------------------------------------------------------------------------
# Login the other user
# -----------------------------------------------------------------------------------------------------------------------


@allure.severity(allure.severity_level.CRITICAL)
@given(u'Given User opens Konsuld URL-RP1')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get("https://dev.konsuld.app/")
    time.sleep(3)
    allure.attach(context.driver.get_screenshot_as_png(), name="Login",
                  attachment_type=AttachmentType.PNG)


@allure.severity(allure.severity_level.CRITICAL)
@when(u'click Log In button-RP1')
def step_impl(context):
    login_button = context.driver.find_element(By.XPATH, "/html/body/div/div[1]/main/div/div/div/div/div/div/button[1]")
    login_button.click()
    time.sleep(2)
    allure.attach(context.driver.get_screenshot_as_png(), name="Login",
                  attachment_type=AttachmentType.PNG)

@allure.severity(allure.severity_level.CRITICAL)
@when(u'enter email and password-RP1')
def step_impl(context):
    email_field = context.driver.find_element(By.ID, 'email')
    email_field.send_keys('nahmed@ohkfhtut.mailosaur.net')
    password_field = context.driver.find_element(By.ID, "password")
    password_field.send_keys('Admin@123')
    allure.attach(context.driver.get_screenshot_as_png(), name="Login",
                  attachment_type=AttachmentType.PNG)

@allure.severity(allure.severity_level.CRITICAL)
@when(u'click Sign In button-RP11')
def step_impl(context):
    sign_in_button = context.driver.find_element(By.XPATH,
                                                 '//*[@id="root"]/div[1]/main/div/div[2]/div[1]/form/div/div/button')
    sign_in_button.click()
    allure.attach(context.driver.get_screenshot_as_png(), name="Login",
                  attachment_type=AttachmentType.PNG)
    time.sleep(8)

@allure.severity(allure.severity_level.CRITICAL)
@when(u'Get the verfication code from mailosaurs inbox-RP1')
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

@allure.severity(allure.severity_level.CRITICAL)
@when(u'enter it in the verification code section-RP1')
def step_impl(context):
    verification_code = context.verification_code

    # Find the verification code input field and enter the code
    verification_code_field = context.driver.find_element(By.XPATH,
                                                          "//input[starts-with(@id, 'verification_code')]")
    verification_code_field.send_keys(verification_code)
    time.sleep(2)
    allure.attach(context.driver.get_screenshot_as_png(), name="Login",
                  attachment_type=AttachmentType.PNG)

@allure.severity(allure.severity_level.CRITICAL)
@when(u'click confirm-RP1')
def step_impl(context):
    confirm_button = context.driver.find_element(By.XPATH,
                                                 "/html/body/div[1]/div[1]/main/div/div[2]/div/div/div/form/div/button")
    confirm_button.click()

    time.sleep(5)
    allure.attach(context.driver.get_screenshot_as_png(), name="Login",
                  attachment_type=AttachmentType.PNG)

@allure.severity(allure.severity_level.CRITICAL)
@when(u'user must login the app-RP1')
def step_impl(context):
    close_tutorial_button = context.driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div/div[1]/button")
    close_tutorial_button.click()
    time.sleep(1)
    allure.attach(context.driver.get_screenshot_as_png(), name="Login",
                  attachment_type=AttachmentType.PNG)

@allure.severity(allure.severity_level.CRITICAL)
@when(u'User is present on the home page-RP1')
def step_impl(context):
   pass

@allure.severity(allure.severity_level.CRITICAL)
@when(u'User navigates to the other users porfile-RP1')
def step_impl(context):
    search_filter = context.driver.find_element(By.XPATH,
                                                "/html/body/div[1]/div[1]/main/div/div[1]/header/div/div/div[1]/div/div/div/div/div/input")
    search_filter.click()

    search_filter.send_keys("chndler")
    time.sleep(1)

    allure.attach(context.driver.get_screenshot_as_png(), name="Comment",
                  attachment_type=AttachmentType.PNG)

@allure.severity(allure.severity_level.CRITICAL)
@then(u'Comments out the recent post-RP1')
def step_impl(context):
    post_option = context.driver.find_element(By.XPATH,
                                              "/html/body/div[1]/div[1]/main/div/div[1]/header/div/div/div[1]/div/div/div[2]/div/ul/li/ul/li[3]/div[2]/div[1]/span")
    post_option.click()
    time.sleep(3)
    allure.attach(context.driver.get_screenshot_as_png(), name="Comment",
                  attachment_type=AttachmentType.PNG)

    user_profile = context.driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/main/div/div[2]/div/div[2]/div/div[2]/div/div/div/div/div/div/div/div[1]/div[1]/div/div[2]/div[1]/span")
    user_profile.click()
    time.sleep(3)



    see_all_activity = context.driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/main/div/div[2]/div/div[2]/div/div[1]/div[4]/div/div[3]/button/span[1]")
    see_all_activity.click()
    time.sleep(3)



    context.driver.execute_script("window.scrollTo(0, 500);")




    like_button = context.driver.find_element(By.XPATH,"//*[@id='root']/div[1]/main/div/div[2]/div/div[2]/div/div[1]/div[3]/div/div/div/div[1]/div/div/div[2]/div/div[2]/div/div/button[1]")
    like_button.click()
    time.sleep(2)

    allure.attach(context.driver.get_screenshot_as_png(), name="Comment",
                  attachment_type=AttachmentType.PNG)

    comment_option = context.driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/main/div/div[2]/div/div[2]/div/div[1]/div[3]/div/div/div/div[1]/div/div/div[2]/div/div[2]/div/div/button[2]")
    comment_option.click()
    time.sleep(2)



    comment_field = context.driver.find_element(By.XPATH,"//textarea[@placeholder='Add a comment...']")
    comment_field.send_keys("Such a wonderful Konsuldation")
    time.sleep(1)

    Post_Comment_button = context.driver.find_element(By.XPATH,"//button[@aria-label='post comment']")
    Post_Comment_button.click()
    time.sleep(1)
    allure.attach(context.driver.get_screenshot_as_png(), name="Comment",
                  attachment_type=AttachmentType.PNG)










    # -----------------------------------------------------------------------------------------------------------------------
    # Login the other user
    # -----------------------------------------------------------------------------------------------------------------------

@allure.severity(allure.severity_level.CRITICAL)
@given(u'Given User opens Konsuld URL-RP2')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get("https://dev.konsuld.app/")
    time.sleep(3)
    allure.attach(context.driver.get_screenshot_as_png(), name="testLoginScreen",
                  attachment_type=AttachmentType.PNG)
    time.sleep(1)
    allure.attach(context.driver.get_screenshot_as_png(), name="login",
                  attachment_type=AttachmentType.PNG)

@allure.severity(allure.severity_level.CRITICAL)
@when(u'click Log In button-RP2')
def step_impl(context):
    login_button = context.driver.find_element(By.XPATH, "/html/body/div/div[1]/main/div/div/div/div/div/div/button[1]")
    login_button.click()
    time.sleep(2)
    allure.attach(context.driver.get_screenshot_as_png(), name="login",
                  attachment_type=AttachmentType.PNG)


@allure.severity(allure.severity_level.CRITICAL)
@when(u'enter email and password-RP2')
def step_impl(context):
    email_field = context.driver.find_element(By.ID, 'email')
    email_field.send_keys('sand-aid@hbiujzoo.mailosaur.net')
    password_field = context.driver.find_element(By.ID, "password")
    password_field.send_keys('Admin@123')
    allure.attach(context.driver.get_screenshot_as_png(), name="login",
                  attachment_type=AttachmentType.PNG)

@allure.severity(allure.severity_level.CRITICAL)
@when(u'click Sign In button-RP2')
def step_impl(context):
    sign_in_button = context.driver.find_element(By.XPATH,
                                                 '//*[@id="root"]/div[1]/main/div/div[2]/div[1]/form/div/div/button')
    sign_in_button.click()
    allure.attach(context.driver.get_screenshot_as_png(), name="login",
                  attachment_type=AttachmentType.PNG)
    time.sleep(8)

@allure.severity(allure.severity_level.CRITICAL)
@when(u'Get the verfication code from mailosaurs inbox-RP2')
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

@allure.severity(allure.severity_level.CRITICAL)
@when(u'enter it in the verification code section-RP2')
def step_impl(context):
    # Retrieve the verification code from context
    verification_code = context.verification_code

    # Find the verification code input field and enter the code
    verification_code_field = context.driver.find_element(By.XPATH,
                                                          "//input[starts-with(@id, 'verification_code')]")
    verification_code_field.send_keys(verification_code)
    time.sleep(2)
    allure.attach(context.driver.get_screenshot_as_png(), name="login",
                  attachment_type=AttachmentType.PNG)

@allure.severity(allure.severity_level.CRITICAL)
@when(u'click confirm-RP2')
def step_impl(context):
    confirm_button = context.driver.find_element(By.XPATH,
                                                 "/html/body/div[1]/div[1]/main/div/div[2]/div/div/div/form/div/button")
    confirm_button.click()

    time.sleep(5)
    allure.attach(context.driver.get_screenshot_as_png(), name="login",
                  attachment_type=AttachmentType.PNG)

@allure.severity(allure.severity_level.CRITICAL)
@when(u'user must login the app-RP2')
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
        allure.attach(context.driver.get_screenshot_as_png(), name="login",
                      attachment_type=AttachmentType.PNG)

        time.sleep(3)

@allure.severity(allure.severity_level.NORMAL)
@when(u'User is present on the home page-RP2')
def step_impl(context):
    time.sleep(2)
    close_tutorial_button = context.driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div/div[1]/button")
    close_tutorial_button.click()
    time.sleep(2)
    allure.attach(context.driver.get_screenshot_as_png(), name="login",
                  attachment_type=AttachmentType.PNG)

@allure.severity(allure.severity_level.CRITICAL)
@when(u'User navigates his own post-RP2')
def step_impl(context):
    profile_dropdown = context.driver.find_element(By.XPATH,"//*[@id='basic-button']")
    profile_dropdown.click()
    time.sleep(1)



    post_and_activity  = context.driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/ul/li[4]/div/span')  # Modify this with the appropriate selector
    post_and_activity.click()
    time.sleep(3)


    # # Scroll to the element
    # context.driver.execute_script("arguments[0].scrollIntoView();", recent_activity)
    #
    # recent_activity_konsuldation = context.driver.find_element(By.XPATH,"(//div[contains(@class, 'MuiBox-root') and contains(@class, 'css-tr1gtc')]//div[contains(@class, 'MuiTypography-root') and contains(@class, 'MuiTypography-semiBold18')])[1]")
    # recent_activity_konsuldation.click()
    # time.sleep(2)

    recent_konsuldation_dropdown = context.driver.find_element(By.XPATH,"//button[contains(@aria-label, 'more options') and contains(@class, 'MuiIconButton-root')]")
    recent_konsuldation_dropdown.click()
    time.sleep(1)
    allure.attach(context.driver.get_screenshot_as_png(), name="ClosePost",
                  attachment_type=AttachmentType.PNG)



@allure.severity(allure.severity_level.CRITICAL)
@then(u'User closes the post-RP2')
def step_impl(context):
    close_konsuldation_button = context.driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/ul/li[2]/div[2]/span")
    close_konsuldation_button.click()
    time.sleep(1)
    allure.attach(context.driver.get_screenshot_as_png(), name="ClosePost",
                  attachment_type=AttachmentType.PNG)


# -----------------------------------------------------------------------------------------------------------------------
# Login the other user
# -----------------------------------------------------------------------------------------------------------------------

@allure.severity(allure.severity_level.CRITICAL)
@given(u'User opens Konsuld URL-RP3')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get("https://dev.konsuld.app/")
    time.sleep(3)
    allure.attach(context.driver.get_screenshot_as_png(), name="testLoginScreen",
                  attachment_type=AttachmentType.PNG)
    time.sleep(1)
    allure.attach(context.driver.get_screenshot_as_png(), name="login",
                  attachment_type=AttachmentType.PNG)


@allure.severity(allure.severity_level.CRITICAL)
@when(u'click Log In button-RP3')
def step_impl(context):
    login_button = context.driver.find_element(By.XPATH, "/html/body/div/div[1]/main/div/div/div/div/div/div/button[1]")
    login_button.click()
    time.sleep(2)
    allure.attach(context.driver.get_screenshot_as_png(), name="login",
                  attachment_type=AttachmentType.PNG)


@allure.severity(allure.severity_level.CRITICAL)
@when(u'enter email and password-RP3')
def step_impl(context):
    email_field = context.driver.find_element(By.ID, 'email')
    email_field.send_keys('nahmed@ohkfhtut.mailosaur.net')
    password_field = context.driver.find_element(By.ID, "password")
    password_field.send_keys('Admin@123')
    allure.attach(context.driver.get_screenshot_as_png(), name="login",
                  attachment_type=AttachmentType.PNG)


@allure.severity(allure.severity_level.CRITICAL)
@when(u'click Sign In button-RP3')
def step_impl(context):
    sign_in_button = context.driver.find_element(By.XPATH,
                                                 '//*[@id="root"]/div[1]/main/div/div[2]/div[1]/form/div/div/button')
    sign_in_button.click()
    allure.attach(context.driver.get_screenshot_as_png(), name="login",
                  attachment_type=AttachmentType.PNG)
    time.sleep(8)

@allure.severity(allure.severity_level.CRITICAL)
@when(u'Get the verfication code from mailosaurs inbox-RP3')
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

@allure.severity(allure.severity_level.CRITICAL)
@when(u'enter it in the verification code section-RP3')
def step_impl(context):
    verification_code = context.verification_code

    # Find the verification code input field and enter the code
    verification_code_field = context.driver.find_element(By.XPATH,
                                                          "//input[starts-with(@id, 'verification_code')]")
    verification_code_field.send_keys(verification_code)
    time.sleep(2)
    allure.attach(context.driver.get_screenshot_as_png(), name="login",
                  attachment_type=AttachmentType.PNG)

@allure.severity(allure.severity_level.CRITICAL)
@when(u'click confirm-RP3')
def step_impl(context):
    confirm_button = context.driver.find_element(By.XPATH,
                                                 "/html/body/div[1]/div[1]/main/div/div[2]/div/div/div/form/div/button")
    confirm_button.click()

    time.sleep(5)
    allure.attach(context.driver.get_screenshot_as_png(), name="login",
                  attachment_type=AttachmentType.PNG)

@allure.severity(allure.severity_level.CRITICAL)
@when(u'user must login the app-RP3')
def step_impl(context):
    close_tutorial_button = context.driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div/div[1]/button")
    close_tutorial_button.click()
    time.sleep(1)
    allure.attach(context.driver.get_screenshot_as_png(), name="login",
                  attachment_type=AttachmentType.PNG)

@allure.severity(allure.severity_level.CRITICAL)
@when(u'User is present on the home page-RP3')
def step_impl(context):
    pass

@allure.severity(allure.severity_level.CRITICAL)
@when(u'User navigates ratings-RP3')
def step_impl(context):
    Konsuldations_option = context.driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/main/div/div[2]/div/div[1]/div/div[1]/div/div[2]/ul/li[3]/div[2]/span")
    Konsuldations_option.click()
    time.sleep(1)

    ratings = context.driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/main/div/div[2]/div/div[1]/div/div[1]/div/div[2]/ul/div/div/div/li/div/span")
    ratings.click()
    time.sleep(1)

    allure.attach(context.driver.get_screenshot_as_png(), name="Rating",
                  attachment_type=AttachmentType.PNG)

@allure.severity(allure.severity_level.CRITICAL)
@then(u'User review the Konsuldation-RP3')
def step_impl(context):
    my_responses = context.driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/main/div/div[2]/div/div[2]/div/div[2]/div/div[1]/div[1]/div/div/button[2]/span[1]")
    my_responses.click()
    time.sleep(1)

    rate_konsuldation_button = context.driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/main/div/div[2]/div/div[2]/div/div[2]/div/div[1]/div[3]/div/div/div/div/div/div[1]/div/div/div[1]/button")
    rate_konsuldation_button.click()
    time.sleep(1)

    rate_one_five_stars = context.driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/main/div/div[2]/div/div[2]/div/div[2]/div/div[1]/div[3]/div/div/div/div/div/div[2]/div/div/div/div/div/div[1]/div/button[5]")
    rate_one_five_stars.click()


    rate_two_four_star = context.driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/main/div/div[2]/div/div[2]/div/div[2]/div/div[1]/div[3]/div/div/div/div/div/div[2]/div/div/div/div/div/div[2]/div/button[4]")
    rate_two_four_star.click()
    time.sleep(1)
    allure.attach(context.driver.get_screenshot_as_png(), name="Rating",
                  attachment_type=AttachmentType.PNG)



    submit_button = context.driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/main/div/div[2]/div/div[2]/div/div[2]/div/div[1]/div[3]/div/div/div/div/div/div[2]/div/div/div/div/div/div[3]/button[2]")
    submit_button.click()
    time.sleep(2)
    allure.attach(context.driver.get_screenshot_as_png(), name="Rating",
                  attachment_type=AttachmentType.PNG)











