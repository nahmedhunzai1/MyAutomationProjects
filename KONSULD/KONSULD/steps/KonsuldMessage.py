from random import random

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

import random

def generate_complex_random_messages():
    messages = [
        "Hey, how are you doing today?",
        "Did you see the latest update? It's great!",
        "LOL, that was hilarious!",
        "Are we still meeting at 7 PM for dinner?",
        "I can't believe it! That was so unexpected!",
        "Just finished a long day of work, need some rest.",
        "Congratulations on your promotion!",
        "Reminder: Your meeting is at 3:30 PM.",
        "Your package is on the way, should arrive in 15 minutes.",
        "This is the best day ever!",
        "Can you send me the report before 5 PM?",
        "Text me when you're ready to go.",
        "Got 99 problems, but this one is easy!",
        "Just finished a workout! Feeling great.",
        "How’s the weather over there today?",
        "I’m so tired, but I have so much work left to do.",
        "Looking forward to the weekend! Got any fun plans?",
        "Price drop alert! The item you were eyeing is 20% off.",
        "Let’s make this happen!",
        "If you need any help, just reach out to me.",
        "I can’t believe it's already the end of the month!",
        "Got a coding challenge coming up. I’m preparing my best code.",
        "My battery is running low, but I’ll reply as soon as I can.",
        "Check out my new shoes, they are super comfortable.",
        "I can't believe it's already the new year!",
        "Just finished a long day at work. Time for Netflix.",
        "Great job on that presentation earlier today!",
        "What’s your favorite app right now? I’m loving [App Name].",
        "Don’t forget to back up your files!",
        "Let’s grab coffee tomorrow! I know a good spot.",
        "I’ve been listening to this new song on repeat.",
        "Are you free tonight? Let’s play a game together.",
        "This is going to be amazing! Let’s do it.",
        "You won the trivia! What’s your prize going to be?",
        "I just bought a new gadget! Can’t wait to try it.",
        "What do you think about UFOs? I just saw one!",
        "Your password was successfully updated. Remember to keep it safe.",
        "Just checked my account. Time to start budgeting.",
        "Relaxing with a cup of tea after a long day.",
        "Help me pick a name for my new dog!",
        "I think I’ve finally figured out this tricky problem.",
        "You have 3 new notifications. Check them out!"
    ]

    # Select one random message from the list
    random_message = random.choice(messages)
    return random_message

# Example usage






@allure.severity(allure.severity_level.CRITICAL)
@Given(u'User opens Konsuld URL-sm')
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

@when(u'click Log In button-sm')
def step_impl(context):
    login_button = context.driver.find_element(By.XPATH, "/html/body/div/div[1]/main/div/div/div/div/div/div/button[1]")
    login_button.click()
    time.sleep(2)
    allure.attach(context.driver.get_screenshot_as_png(), name="testMessageInAccount",
                  attachment_type=AttachmentType.PNG)

@when(u'enter email and password-sm')
def step_impl(context):
    email_field = context.driver.find_element(By.ID, 'email')
    email_field.send_keys('sand-aid@hbiujzoo.mailosaur.net')
    password_field = context.driver.find_element(By.ID, "password")
    password_field.send_keys('Admin@123')
    allure.attach(context.driver.get_screenshot_as_png(), name="testMessageInAccount",
                  attachment_type=AttachmentType.PNG)

@when(u'click Sign In button-sm')
def step_impl(context):
    sign_in_button = context.driver.find_element(By.XPATH,
                                                 '//*[@id="root"]/div[1]/main/div/div[2]/div[1]/form/div/div/button')
    sign_in_button.click()
    allure.attach(context.driver.get_screenshot_as_png(), name="testMessageInAccount",
                  attachment_type=AttachmentType.PNG)
    time.sleep(8)


@when(u'Get the verfication code from mailosaurs inbox-sm')
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


@when(u'enter it in the verification code section-sm')
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




@when(u'click confirm-sm')
def step_impl(context):
    confirm_button = context.driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/main/div/div[2]/div/div/div/form/div/button")
    confirm_button.click()

    time.sleep(5)
    allure.attach(context.driver.get_screenshot_as_png(), name="testMessageInAccount",
                  attachment_type=AttachmentType.PNG)

    time.sleep(3)

    close_tutorial_button = context.driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div/div[1]/button")
    close_tutorial_button.click()
    time.sleep(1)
    allure.attach(context.driver.get_screenshot_as_png(), name="testMessageInAccount",
                  attachment_type=AttachmentType.PNG)

@when(u'click the message option-sm')
def step_impl(context):
    message_button = context.driver.find_element(By.XPATH,
                                                     "//*[@id='root']/div[1]/main/div/div[1]/header/div/div/div[2]/div[1]/div[2]/div/span")
    message_button.click()
    time.sleep(1)

    allure.attach(context.driver.get_screenshot_as_png(), name="testMessageInAccount",
                  attachment_type=AttachmentType.PNG)


@when(u'click Send New Message option-sm')
def step_impl(context):
    new_message_button = context.driver.find_element(By.XPATH,"//*[@id='root']/div[1]/main/div/div[2]/div/div[2]/div/div[1]/div/h5/div/div/button")
    new_message_button.click()
    time.sleep(1)

    allure.attach(context.driver.get_screenshot_as_png(), name="testMessageInAccount",
                  attachment_type=AttachmentType.PNG)

    message_user = "Oliver"

    search_user_field = context.driver.find_element(By.XPATH,"//*[@id='search']")
    search_user_field.send_keys(message_user)
    time.sleep(2)

    allure.attach(context.driver.get_screenshot_as_png(), name="testMessageInAccount",
                  attachment_type=AttachmentType.PNG)






@when(u'click message option to first newtwork-sm')
def step_impl(context):
    user_message_button = context.driver.find_element(By.XPATH,
                                                      "/html/body/div[1]/div[1]/main/div/div[2]/div/div[2]/div/div[2]/div/div/div/button/span[1]")
    user_message_button.click()
    time.sleep(1)

    allure.attach(context.driver.get_screenshot_as_png(), name="testMessageInAccount",
                  attachment_type=AttachmentType.PNG)

@when(u'Enter a message and clock send button-sm')
def step_impl(context):
    random_msg = generate_complex_random_messages()

    message_field = context.driver.find_element(By.XPATH,"//*[@id='message']")
    message_field.send_keys(random_msg)

    send_button = context.driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/main/div/div[2]/div/div[2]/div/div[2]/div/div/div[2]/div/div[3]/div[3]/div/button")
    send_button.click()
    time.sleep(4)

    allure.attach(context.driver.get_screenshot_as_png(), name="testMessageInAccount",
                  attachment_type=AttachmentType.PNG)




@given(u'User opens Konsuld URL-sm1')
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


@when(u'click Log In button-sm1')
def step_impl(context):
    login_button = context.driver.find_element(By.XPATH, "/html/body/div/div[1]/main/div/div/div/div/div/div/button[1]")
    login_button.click()
    time.sleep(2)
    allure.attach(context.driver.get_screenshot_as_png(), name="testMessageInAccount",
                  attachment_type=AttachmentType.PNG)


@when(u'enter email and password-sm1')
def step_impl(context):
    email_field = context.driver.find_element(By.ID, 'email')
    email_field.send_keys('nahmed@ohkfhtut.mailosaur.net')
    password_field = context.driver.find_element(By.ID, "password")
    password_field.send_keys('Admin@123')
    allure.attach(context.driver.get_screenshot_as_png(), name="testMessageInAccount",
                  attachment_type=AttachmentType.PNG)


@when(u'click Sign In button-sm1')
def step_impl(context):
    sign_in_button = context.driver.find_element(By.XPATH,
                                                 '//*[@id="root"]/div[1]/main/div/div[2]/div[1]/form/div/div/button')
    sign_in_button.click()
    allure.attach(context.driver.get_screenshot_as_png(), name="testMessageInAccount",
                  attachment_type=AttachmentType.PNG)
    time.sleep(8)


@when(u'Get the verfication code from mailosaurs inbox-sm1')
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


@when(u'enter it in the verification code section-sm1')
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






@when(u'click confirm-sm1')
def step_impl(context):
    confirm_button = context.driver.find_element(By.XPATH,
                                                 "/html/body/div[1]/div[1]/main/div/div[2]/div/div/div/form/div/button")
    confirm_button.click()

    time.sleep(5)
    allure.attach(context.driver.get_screenshot_as_png(), name="testMessageInAccount",
                  attachment_type=AttachmentType.PNG)



@when(u'user must login the app-sm1')
def step_impl(context):
    close_tutorial_button = context.driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div/div[1]/button")
    close_tutorial_button.click()
    time.sleep(1)
    allure.attach(context.driver.get_screenshot_as_png(), name="testMessageInAccount",
                      attachment_type=AttachmentType.PNG)

@when(u'User is present on the home page-sm1')
def step_impl(context):
    pass

@when(u'User opens messages-sm1')
def step_impl(context):
    message_button = context.driver.find_element(By.XPATH,
                                                 "//*[@id='root']/div[1]/main/div/div[1]/header/div/div/div[2]/div[1]/div[2]/div/span")
    message_button.click()
    time.sleep(1)
    allure.attach(context.driver.get_screenshot_as_png(), name="testMessageInAccount",
                  attachment_type=AttachmentType.PNG)

    new_message_button = context.driver.find_element(By.XPATH,
                                                     "//*[@id='root']/div[1]/main/div/div[2]/div/div[2]/div/div[1]/div/h5/div/div/button")
    new_message_button.click()
    time.sleep(1)

    message_user = "chndler"

    search_user_field = context.driver.find_element(By.XPATH, "//*[@id='search']")
    search_user_field.send_keys(message_user)
    time.sleep(3)

    user_message_button = context.driver.find_element(By.XPATH,
                                                      "/html/body/div[1]/div[1]/main/div/div[2]/div/div[2]/div/div[2]/div/div/div/button/span[1]")
    user_message_button.click()
    time.sleep(1)
    allure.attach(context.driver.get_screenshot_as_png(), name="testMessageInAccount",
                  attachment_type=AttachmentType.PNG)



@when(u'replies to the received message-sm1')
def step_impl(context):

    try:
        random_msg2 = generate_complex_random_messages()

        message_field = context.driver.find_element(By.XPATH, "//*[@id='message']")
        message_field.send_keys(random_msg2)
        allure.attach(context.driver.get_screenshot_as_png(), name="testMessageInAccount",
                  attachment_type=AttachmentType.PNG)

        send_button = context.driver.find_element(By.XPATH,
                                              "/html/body/div[1]/div[1]/main/div/div[2]/div/div[2]/div/div[2]/div/div/div[2]/div/div[3]/div[3]/div/button")
        send_button.click()
        time.sleep(4)

        allure.attach(context.driver.get_screenshot_as_png(), name="testMessageInAccount",
                  attachment_type=AttachmentType.PNG)
    except Exception as e:
        print(f"Error occurred : {e}")
        return None







