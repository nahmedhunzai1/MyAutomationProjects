import allure
import pytest
from lib2to3.fixes.fix_input import context

from allure_commons.model2 import Attachment
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time


chrome_options = Options()
chrome_options.add_argument("--incognito")
driver_path = "../driver/chrome-mac-arm64/Google Chrome for Testing.app"


class Testwhoz:
    @allure.severity(allure.severity_level.NORMAL)
    def test_launch_chrome(self ):
        context.driver = webdriver.Chrome()
        context.driver.maximize_window()
        context.driver.get("https://uat.app.whoz.co")
        time.sleep(6)
        status = context.driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/header/div/div/div[1]').is_displayed()

        if status == True:
            assert True
        else:
            assert False

    @allure.severity(allure.severity_level.CRITICAL)
    def test_login_email_password(self):
        email_field = context.driver.find_element(By.ID,'email')
        email_field.send_keys('nahmed@technologyrivers.com')

        pass_field = context.driver.find_element(By.ID,'password')
        pass_field.send_keys('Admin@1234')
        time.sleep(2)

        login_button = context.driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/main/div[2]/div/div/div/div/div[1]/form/div[7]/button')
        login_button.click()
        time.sleep(6)

        try:
            # Try to locate the element
            email_display = context.driver.find_element(By.XPATH,
                                                '/html/body/div[1]/div[2]/header/div/div/div[2]/div[2]/div/div').text
        except NoSuchElementException:
            allure.attach(context.driver.get_screenshot_as_png(), name="testLoginScreen", attachment_type=AttachmentType.PNG)
            pytest.fail("Unable to Login")


    @allure.severity(allure.severity_level.CRITICAL)
    def test_loginGoogle(self):
        login_with_google = context.driver.find_element(By.XPATH,
                                                        '//*[@id="root"]/div[2]/div/main/div[2]/div/div/div/div/div[1]/form/div[2]/button/p')
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

    @allure.severity(allure.severity_level.NORMAL)
    def test_login_random(self):
        pytest.skip("skipping test .. later I will implement" )




