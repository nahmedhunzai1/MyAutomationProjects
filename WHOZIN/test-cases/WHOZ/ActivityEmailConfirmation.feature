Feature: Triggering emails

  @CreateActivity
  Scenario: Activity Email verification
    Given The browser is launched
    When Whoz App is opened
    And User login the Whoz app
    And Creates Activity successfully
    Then Navigates to the view activity screen

  @MailTrap
  Scenario: Mailtrap part
    Given Open the mailtrap
    When Login into the mailtrap
    And Navigate to Mailtrap Inbox
    Then Verify activity email is sent to the users
