Feature: User Login Step
  Background: Common Steps
     Given launched chrome browser
     When User navigates to the login page
     #step paremeters#
     And Enter username1 "admin@scanmygolfball.com" and password1 "Rivers"
     And Click on Login button1

  Scenario: Verify Active Users Sections
    Given User is on the Admin Dashboard
    When User navigates to the Active User section
    And User must observe that active users is appearing correct
    And User must observe that the Past 24 Hours Users are appearing Correct
    And User must observe that the Past 7 days Users are appearing Correct
    And User must observe that the Past 30 days Users are appearing Correct
    And Verify the Active Users Date filter is working



