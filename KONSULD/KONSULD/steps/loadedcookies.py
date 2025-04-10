import pickle
import time
import json
import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from behave import *

chrome_options = Options()
chrome_options.add_argument("--incognito")
driver_path = "/Users/jerry/Desktop/QA-Automation/WHOZIN/driver/chrome-mac-arm64/chromedriver"

@allure.severity(allure.severity_level.CRITICAL)
@Given(u'User opens Konsuld URL with cookies-lcf')
def step_impl(context):
    # Load auth token from pickle file
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

    time.sleep(10)
