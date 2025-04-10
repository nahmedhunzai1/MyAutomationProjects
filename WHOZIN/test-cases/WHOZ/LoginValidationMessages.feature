Feature: Manual Login
  Background: Common Steps
    Given Launch Chrome Browser2
    When Open the Login Page2
    Then Verify if the correct login page is opened2

  Scenario: Google Login Verification1
    And Invalid email message is appearing
    And Wrong password message is appearing