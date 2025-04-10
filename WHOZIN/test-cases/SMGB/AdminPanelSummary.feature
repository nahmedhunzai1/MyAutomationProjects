Feature: User Login Step
  Background: Common Steps
     Given launched chrome browser2
     When User navigates to the login page2
     #step paremeters#
     And Enter username2 "admin@scanmygolfball.com" and password2 "Rivers"
     And Click on Login button2


  Scenario: Verify Summary Sections
    Given User is on the Admin Dashboard2
    When User navigates to the Summary section2
    Then check that the registered user section is working fine
    And check that the guest user section is working fine
    And check that the Balls section is working fine
    And check that the Scanner count is visible
    And check that the Scan Results section is working fine